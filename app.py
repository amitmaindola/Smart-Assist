from crypt import methods
from operator import truediv
from flask import *
from transformers import pipeline
import moviepy.editor
from question_answer.question_generator import generate_questions
import speech_recognition as sr
import os


app = Flask(__name__)

path = 'video.mp4'
video = moviepy.editor.VideoFileClip(path)
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


@app.route("/")
def landing():
    return render_template('home.html', text="Akshar Betichod")

@app.route("/home", methods = ['GET'])
def home():
    return render_template('upload.html')

@app.route('/home', methods = ['POST'])
def success():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        path = f.filename
        video = moviepy.editor.VideoFileClip(path)
        video_to_audio(path)
        text = audio_to_text("demo.wav")
        # # summary_text = text_summary(text)
        summary_text = "This is summary"
        text = "People celebrate Holi with utmost fervour and enthusiasm, especially in North India. One day before Holi, people conduct a ritual called Holika Dahan. In this ritual, people pile heaps of wood in public areas to burn. It symbolizes the burning of evil powers revising the story of Holika and King Hiranyakashyap. Furthermore, they gather around the Holika to seek blessings and offer their devotion to God."
        questions_data = generate_questions(text)
        print(questions_data)
        for item in questions_data:
            item['question']=item['question'].replace("<pad>", "")
            item['answer']=item['answer'].replace("<pad>", "")
        return render_template('summary.html', actualText = text, summary_text = summary_text, questions_data = questions_data)

@app.route("/summary", methods = ['GET'])
def summary():
    return render_template('summary.html')

if __name__ == "__main__":
    app.run(debug=True, port=3000)