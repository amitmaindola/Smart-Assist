from crypt import methods
from operator import truediv
from flask import *
from transformers import pipeline
import moviepy.editor
from question_answer.question_generator import generate_questions
import speech_recognition as sr
import os
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

#text_to_summarizer
def text_summary(text):
    summarizer = pipeline("summarization", model="t5-base", tokenizer="t5-base", framework="tf")
    summary_text = summarizer(text, max_length=text.length//2, min_length=5, do_sample=False)[0]['summary_text']
    print(summary_text)

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
        summary_text = "This is summary"
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
        return render_template('summary.html', actualText = text, summary_text = summary_text, questions_data = questions_data, keywords = keywords)

@app.route("/summary", methods = ['GET'])
def summary():
    return render_template('summary.html')

if __name__ == "__main__":
    app.run(debug=True, port=3000)