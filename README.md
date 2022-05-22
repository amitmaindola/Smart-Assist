# Theme
Education

# Smart-Assist
This is the github repositry of a website made by Team Hufflepuffs(group of students of IIT Mandi) for the event frosthack in the technical fest of IIT Mandi XPECTO'22.
This website is based on the theme education and is particulary for student's use.
Smart assist basically creates a study environment for the students and ease their problem of reading long textual paragraphs or listening to long video lectures by provide a short summary of the whole.
This summary is processed by using natural language processing and deep learning. By the use of natural language toolkit we can find the important questions with their answers and some important keywords related to the paragraph.

# Objective
1. It is helpful for endtime revision for a student. Now students can get short summary, important questions and answers, keywords and their meanings from
   video lectures, audio lectures and texts.
2. Sometimes it’s too boring to read long long paragraphs, watching long videos, or hearing long audios. And sometimes even we do not have enough time for      the same.
3. It is also helpful for the teachers to generate questions for the exams by using their own video lectures itself.

# Techstack
1. NLP - Natural Language Processing for various features
2. Flask - Backend
3. Tensorflow and Pytorch - Libraries to implement NLP
4. TML, CSS, JavaScript - Frontend

# Working
1. First you have to clone the repository.
2. If you don't have a virtual environment then run the command `pip install virtualenv`.
3. Create virtual environment by using `python -m virtalenv env` and then `source env/Scripts/activate`(for Windows Users) and `source ./env/bin/activate`(for Linux users).
4. Next use the `pip install -r requirements.txt` command or `pip3 install requirements.txt` to install all the libraries and dependencies
5. Now write the commands `pip install transformers==3.0.0` ,`pip install nltk` and `pip install nlp`.
6. After installing nltk do `python -m nltk.downloader punkt`
7. Now to run the website go inside the smart assist directory and type `python app.py`.
8. Now the website will start running locally and bingo u can enjoy the various features of the website.

# Video Demo
https://youtu.be/t4hJB6XJ4sY

# Landing Page :
![Screenshot 2022-05-23 at 2 00 29 AM](https://user-images.githubusercontent.com/79039452/169714623-b1be991f-6bbd-4216-b599-88567106d37d.png)
# Video/Text/Audio uploading page:
![Screenshot 2022-05-23 at 2 01 02 AM](https://user-images.githubusercontent.com/79039452/169714646-c5fd62c2-47ab-4261-bd9a-07a34be6ee3d.png)
# Summarization Result:
![Screenshot 2022-05-23 at 1 59 56 AM](https://user-images.githubusercontent.com/79039452/169714606-77cc344d-7651-4502-af7d-0b5e5bb0c97e.png)
# Question Answer Generation:
![Screenshot 2022-05-23 at 2 20 05 AM](https://user-images.githubusercontent.com/79039452/169715275-8cffede3-4d8f-4f0d-bb99-ed1e3897f1fe.png)
# Important Tools:
![Screenshot 2022-05-23 at 2 02 09 AM](https://user-images.githubusercontent.com/79039452/169714676-15c67781-a97e-4a7e-866a-92748615fea9.png)
# About
![Screenshot 2022-05-23 at 2 02 58 AM](https://user-images.githubusercontent.com/79039452/169714704-547ddf49-673e-46fc-b519-3814ff15a4f9.png)
