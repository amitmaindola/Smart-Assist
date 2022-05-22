from transformers import pipeline
# import os
# os.environ["CUDA_VISIBLE_DEVICES"] = "0"
import moviepy.editor
import speech_recognition as sr
#video
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
def text_summary():
    summarizer = pipeline("summarization", model="t5-base", tokenizer="t5-base", framework="tf")
    summary_text = summarizer(text, max_length=100, min_length=5, do_sample=False)[0]['summary_text']
    print(summary_text)

video_to_audio("video.mp4")
audio_to_text("demo.wav")