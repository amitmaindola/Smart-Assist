from crypt import methods
from operator import truediv
from flask import *
from transformers import pipeline
import moviepy.editor
from question_answer.question_generator import generate_questions
from summary import summarizer
import speech_recognition as sr
import os
import nltk
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer



app = Flask(__name__)

#video_to_audio

def video_to_audio(path):
    video = moviepy.editor.VideoFileClip(path)
    aud = video.audio
    aud.write_audiofile("demo.wav")
    print("--End--")

#audio_to_text
def audio_to_text(path):
    text=''
    r=sr.Recognizer()
    with sr.AudioFile(path) as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data)
        print(text)
        return text

# Keywords Finder
def keyword_generator(text,range, top_n):
    n_gram_range = (1, range)
    stop_words = "english"
    count = CountVectorizer(ngram_range=n_gram_range, stop_words=stop_words).fit([text])
    candidates = count.get_feature_names_out()
    model = SentenceTransformer('distilbert-base-nli-mean-tokens')
    doc_embedding = model.encode([text])
    candidate_embeddings = model.encode(candidates)
    distances = cosine_similarity(doc_embedding, candidate_embeddings)
    keywords = [candidates[index] for index in distances.argsort()[0][-top_n:]]
    print(keywords)
    return keywords

@app.route("/")
def landing():
    return render_template('home.html', text="Akshar Betichod")

@app.route("/home", methods = ['GET'])
def home():
    return render_template('upload.html')

@app.route('/home', methods = ['POST'])
def success():
    if request.method == 'POST':
        fileType = request.form.get('type')
        if(fileType=="audio" or fileType=="video"):
            f = request.files['file']
            if(fileType=="video"):
                f.save(f.filename)
                path = f.filename
                video = moviepy.editor.VideoFileClip(path)
                video_to_audio(path)
            else:
                f.save("demo.wav")
            text = audio_to_text("demo.wav")
        # # summary_text = text_summary(text)
        else:
            text = request.form.get("inputText")
        # Generating Questions
        questions_data = generate_questions(text)
        print(questions_data)
        for item in questions_data:
            item['question']=item['question'].replace("<pad>", "")
            item['answer']=item['answer'].replace("<pad>", "")
        # Generating Keywords
        keywords=[]
        keywords.append(keyword_generator(text, 1, 5))
        keywords.append(keyword_generator(text, 2, 3))
        keywords.append(keyword_generator(text, 3, 1))
        ch1 = len(text);
        w1 = len(text.split())
        sentences = nltk.sent_tokenize(text)
        summaryLen = len(sentences)
        summary_text=summarizer(text, summaryLen//2)
        ch2 = len(summary_text);
        w2 = len(summary_text.split())
        print(summary_text)

        return render_template('summary.html', actualText = text, summary_text = summary_text, questions_data = questions_data, keywords = keywords, w1 = w1, w2 = w2, ch1 = ch1, ch2 = ch2)

@app.route("/summary", methods = ['GET'])
def summary():
    return render_template('summary.html')

@app.route("/graph", methods=['GET'])
def graph():
    return render_template('graph.html')

@app.route("/calculator", methods=['GET'])
def graph():
    return render_template('calculator.html')

if __name__ == "__main__":
    app.run(debug=True, port=3000)