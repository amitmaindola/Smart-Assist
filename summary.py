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
pip install -U pip setuptools wheel
pip install -U spacy
python -m spacy download en_core_web_sm

import spacy
from collections import Counter
from string import punctuation
nlp = spacy.load("en_core_web_lg")
import en_core_web_lg
nlp = en_core_web_lg.load()
def top_sentence(text, limit):
    keyword = []
    pos_tag = ['PROPN', 'ADJ', 'NOUN', 'VERB']
    doc = nlp(text.lower())
    for token in doc:
        if(token.text in nlp.Defaults.stop_words or token.text in punctuation):
            continue
        if(token.pos_ in pos_tag):
            keyword.append(token.text)
    
    freq_word = Counter(keyword)
    max_freq = Counter(keyword).most_common(1)[0][1]
    for w in freq_word:
        freq_word[w] = (freq_word[w]/max_freq)
        
    sent_strength={}
    for sent in doc.sents:
        for word in sent:
            if word.text in freq_word.keys():
                if sent in sent_strength.keys():
                    sent_strength[sent]+=freq_word[word.text]
                else:
                    sent_strength[sent]=freq_word[word.text]
    
    summary = []
    
    sorted_x = sorted(sent_strength.items(), key=lambda kv: kv[1], reverse=True)
    
    counter = 0
    for i in range(len(sorted_x)):
        summary.append(str(sorted_x[i][0]).capitalize())

        counter += 1
        if(counter >= limit):
            break
            
    return ' '.join(summary)
text = 'Machine learning (ML) is the scientific study of algorithms and statistical models that computer systems use to progressively improve their performance on a specific task. Machine learning algorithms build a mathematical model of sample data, known as “training data”, in order to make predictions or decisions without being explicitly programmed to perform the task. Machine learning algorithms are used in the applications of email filtering, detection of network intruders, and computer vision, where it is infeasible to develop an algorithm of specific instructions for performing the task. Machine learning is closely related to computational statistics, which focuses on making predictions using computers. The study of mathematical optimization delivers methods, theory and application domains to the field of machine learning. Data mining is a field of study within machine learning and focuses on exploratory data analysis through unsupervised learning. In its application across business problems, machine learning is also referred to as predictive analytics.'
p = len(list (text.sents))
print(top_sentence(text,p/2))

video_to_audio("video.mp4")
audio_to_text("demo.wav")