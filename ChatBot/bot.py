# Meet Pybot: your friend

import nltk
import warnings
import os
import webbrowser

warnings.filterwarnings("ignore")
# nltk.download() # for downloading packages
# import tensorflow as tf
import numpy as np
import random
import string  # to process standard python strings

f = open('nlp python answer finals.txt', 'r', errors='ignore')
m = open('modules pythons.txt', 'r', errors='ignore')
a = open('Vedant.txt', 'r', errors='ignore')

checkpoint = "./chatbot_weights.ckpt"
# session = tf.InteractiveSession()
# session.run(tf.global_variables_initializer())
# saver = tf.train.Saver()
# saver.restore(session, checkpoint)

raw = f.read()
rawone = m.read()
rawtwo = a.read()
raw = raw.lower()  # converts to lowercase
rawone = rawone.lower()  # converts to lowercase
rawtwo = rawtwo.lower()
nltk.download('punkt')  # first-time use only
nltk.download('wordnet')  # first-time use only
sent_tokens = nltk.sent_tokenize(raw)  # converts to list of sentences
word_tokens = nltk.word_tokenize(raw)  # converts to list of words
sent_tokensone = nltk.sent_tokenize(rawone)  # converts to list of sentences
word_tokensone = nltk.word_tokenize(rawone)  # converts to list of words
sent_tokenstwo = nltk.sent_tokenize(rawtwo)  # converts to list of sentences
word_tokenstwo = nltk.word_tokenize(rawtwo)  # converts to list of words

sent_tokens[:2]
sent_tokensone[:2]
sent_tokenstwo[:2]

word_tokens[:5]
word_tokensone[:5]
word_tokenstwo[:5]

lemmer = nltk.stem.WordNetLemmatizer()


def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]


remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)


def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


Introduce_Ans = ["My name is ChatterBot. I have been created by Vedant Nichal.",
                 "My name is Chatterbot you can called me Bot. I have been created by Vedant Nichal.",
                 "I'm ChatterBot :) I have been created by Vedant Nichal. ",
                 "My name is Chatterbot. and my nickname is Bot and i am happy to solve your queries :) I have been created by Vedant Nichal."]
GREETING_INPUTS = ("hello", "hi", "hiii", "hii", "hiiii", "hiiii", "greetings", "sup", "what's up", "hey",)
GREETING_RESPONSES = ["hi", "hey", "hii there", "hi there", "hello", "I am glad! You are talking to me"]
Basic_Q = ("what is python ?", "what is python", "what is python?", "what is python.")
Basic_Ans = "Python is a high-level, interpreted, interactive and object-oriented scripting programming language python is designed to be highly readable It uses English keywords frequently where as other languages use punctuation, and it has fewer syntactical constructions than other languages."
Basic_Om = ("what is module", "what is module.", "what is module ", "what is module ?", "what is module?",
            "what is module in python", "what is module in python.", "what is module in python?",
            "what is module in python ?")
Basic_AnsM = ["Consider a module to be the same as a code library.",
              "A file containing a set of functions you want to include in your application.",
              "A module can define functions, classes and variables. A module can also include runnable code. Grouping related code into a module makes the code easier to understand and use."]


# Checking for greetings
def greeting(sentence):
    """If user's input is a greeting, return a greeting response"""
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)


# Checking for Basic_Q
def basic(sentence):
    for word in Basic_Q:
        if sentence.lower() == word:
            return Basic_Ans


# Checking for Basic_QM
def basicM(sentence):
    """If user's input is a greeting, return a greeting response"""
    for word in Basic_Om:
        if sentence.lower() == word:
            return random.choice(Basic_AnsM)


# Checking for Introduce
def IntroduceMe(sentence):
    return random.choice(Introduce_Ans)


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Generating response
def response(user_response):
    robo_response = ''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if (req_tfidf == 0):
        robo_response = robo_response + "I am sorry! I don't understand you...You can search google for the answer though."
        webbrowser.open("https:\\google.com")
        return robo_response
    else:
        robo_response = robo_response + sent_tokens[idx]
        return robo_response


# Generating response
def responseone(user_response):
    robo_response = ''
    sent_tokensone.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokensone)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if (req_tfidf == 0):
        robo_response = robo_response + "I am sorry! I don't understand you...You can search google for the answer though.", webbrowser.open("https:\\google.com")
        return robo_response
    else:
        robo_response = robo_response + sent_tokensone[idx]
        return robo_response


def chat(user_response):
    user_response = user_response.lower()
    keyword = " module "
    keywordone = " module"
    keywordsecond = "module "

    if (user_response != 'bye'):
        if (user_response == 'thanks' or user_response == 'thank you'):
            flag = False
            # print("ROBO: You are welcome..")
            return "You're welcome...I'm glad that I could help you!"
        elif (basicM(user_response) != None):
            return basicM(user_response)
        else:
            if (user_response.find(keyword) != -1 or user_response.find(keywordone) != -1 or user_response.find(
                    keywordsecond) != -1):
                # print("ROBO: ",end="")
                # print(responseone(user_response))
                return responseone(user_response)
                sent_tokensone.remove(user_response)
            elif (greeting(user_response) != None):
                # print("ROBO: "+greeting(user_response))
                return greeting(user_response)
            elif (user_response.find("your name") != -1 or user_response.find(" your name") != -1 or user_response.find(
                    "your name ") != -1 or user_response.find(" your name ") != -1) or user_response.find(
                "who are you") != -1:
                return IntroduceMe(user_response)
            elif (basic(user_response) != None):
                return basic(user_response)
            elif (user_response == 'what is cricket'):
                return "Cricket is a sport which is played between two teams of eleven players each who score runs (points). This is done by hitting the ball across the boundary, or by one team's players running between two objects called wickets as many times as possible before the other team gets the ball to either wicket to stop them from scoring runs."
            elif (user_response == 'what is coronavirus'):
                return "Coronavirus disease (COVID-19) is an infectious disease caused by a newly discovered coronavirus. Most people infected with the COVID-19 virus will experience mild to moderate respiratory illness and recover without requiring special treatment."
            elif user_response == 'what is ai':
                return "Artificial intelligence (AI) is wide-ranging branch of computer science concerned with building smart machines capable of performing tasks that typically require human intelligence."
            elif user_response == 'what is shinchan':
                return "Shin-chan is a Japanese manga series written and illustrated by Yoshito Usui. It follows the adventures of the five-year-old Shinnosuke Shin Nohara and his parents, baby sister, dog, neighbours, and friends and is set in Kasukabe, Saitama Prefecture of Japan."
            elif user_response == 'who is rohit sharma':
                return "Rohit Gurunath Sharma is an Indian international cricketer who plays for Mumbai in domestic cricket and captains Mumbai Indians in the Indian Premier League as a right-handed batsman and an occasional right-arm off break bowler. He is the vice-captain of the Indian national team in limited-overs formats."
            elif user_response == 'who is virat kohli':
                return "Virat is an Indian cricketer and the current captain of the India national team. A right-handed top-order batsman, Kohli is regarded as one of the best batsmen in the world. He plays for Royal Challengers Bangalore in the Indian Premier League (IPL), and has been the team's captain since 2013. "
            elif user_response == 'what is football':
                return "Association football, more commonly known as football or soccer, is a team sport played with a spherical ball between two teams of 11 players. It is played by approximately 250 million players in over 200 countries and dependencies, making it the world's most popular sport."
            elif user_response == 'what is an image':
                return "An image is an artifact that depicts visual perception, such as a photograph or other two-dimensional picture, that resembles a subject—usually a physical object—and thus provides a depiction of it. "
            elif user_response == 'what is animation':
                return "Animation is a method in which figures are manipulated to appear as moving images. In traditional animation, images are drawn or painted by hand on transparent celluloid sheets to be photographed and exhibited on film. Today, most animations are made with computer-generated imagery (CGI)."
            elif user_response == 'what is cmd':
                return "cmd.exe is the default command-line interpreter for OS/2, eComStation, ArcaOS, Microsoft Windows, and the ReactOS operating systems. The name refers to its executable filename. It is also commonly referred to as cmd or the Command Prompt, referring to the default window title on Windows. "
            elif user_response == 'what is doraemon':
                return "Doraemon is a Japanese manga series written and illustrated by Fujiko Fujio, the pen name of the duo Hiroshi Fujimoto and Motoo Abiko. The series has also been adapted into a successful anime series and media franchise."
            elif user_response == 'open notepad':
                codePath = 'A:\\Windows\\System32\\notepad.exe'
                os.startfile(codePath)
            elif user_response == 'play music':
                music_dir = 'G:\\Songs\\1234'
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))
            elif user_response == 'open paint':
                codePath = 'A:\\Windows\\system32\\mspaint.exe'
                os.startfile(codePath)
            elif user_response == 'show me the indian flag':
                codePath = 'A:\\Users\\anvit\\Downloads\\download.png'
                os.startfile(codePath)
            elif user_response == 'what can you do':
                return "Well, I can do a lot of stuff like searching things for you, opening some applications, playing songs, etc. I try my best to help you but sometimes i don't understand"
            elif user_response == 'open skolaro':
                webbrowser.open("https:\\apps.skolaro.com")
                return "Sure!"
            elif user_response == "if you don't know the answer then what should i do":
                webbrowser.open("https:\\google.com")
                return "You can search the Google for the answer."
            elif user_response == "what is pycharm":
                return "PyCharm is an integrated development environment used in computer programming, specifically for the Python language. It is developed by the Czech company JetBrains."
            elif user_response == "i want to play a game":
                codePath = 'A:\\Python Projects\\Kivy\\PingPong\\main.py'
                os.startfile(codePath)
                return "You can play Ping Pong Game. It has been created by Vedant Nichal."
            elif user_response == "do i have anything scheduled for today evening":
                return "No, you are free today evening...enjoy!!!"
            elif user_response == "how have you been created":
                return "Vedant\'s ChatterBot is a chatbot for answering some basic questions.\nIt is based on retrival-based NLP using pythons NLTK tool-kit module\nGUI is based on Tkinter.\nIt has been created by Vedant Nichal.\nUser created Neural Network helps recieve data"
            elif user_response == "what is ipl":
                return "The Indian Premier League is a professional Twenty20 cricket league in India contested during March or April and May of every year by eight teams representing eight different cities in India. The league was founded by the Board of Control for Cricket in India in 2008. "
            elif user_response == "what is an app":
                return "A mobile application, also referred to as a mobile app or simply an app, is a computer program or software application designed to run on a mobile device such as a phone, tablet, or watch. Apps were originally intended for productivity assistance such as email, calendar, and contact databases, but the public demand for apps caused rapid expansion into other areas such as mobile games, factory automation, GPS and location-based services, order-tracking, and ticket purchases, so that there are now millions of apps available."
            elif user_response == "how are you":
                return "I am always good. How may I help you?"
            elif user_response == "tell me some entertainment apps":
                return "Amazon Prime, Netflix, Youtube"
            elif user_response == "open youtube":
                webbrowser.open("https:\\youtube.com")
                return "Sure!"
            elif user_response == "open google":
                webbrowser.open("https:\\google.com")
                return "Sure!"
            elif user_response == "what is amazon":
                return "Amazon.com, Inc., is an American multinational technology company based in Seattle, Washington. Amazon focuses on e-commerce, cloud computing, digital streaming, and artificial intelligence. It is considered one of the Big Four technology companies, along with Google, Apple, and Facebook."
            else:
                # print("ROBO: ",end="")
                # print(response(user_response))
                return response(user_response)
                sent_tokens.remove(user_response)
