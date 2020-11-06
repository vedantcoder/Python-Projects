import pyttsx3
import speech_recognition as sr
import datetime
import os
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    print("JARVIS: ", audio)


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good morning sir! Have a good Day!")

    elif 12 <= hour < 18:
        speak("Good Afternoon")

    else:
        speak("Good Evening! Hope you have had a good day so far!")

    speak("I am Jarvis. I have been created by Vedant Nichal. How may I help you?")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You: {query}\n")


    except Exception as e:
        print(e)
        print("Sorry, Please say that again...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takecommand().lower()

        if 'open youtube' in query:
            webbrowser.open("https:\\www.youtube.com")

        elif 'open google' in query:
            webbrowser.open("https:\\www.google.com")

        elif 'play music' in query:
            music_dir = 'G:\\Songs\\1234'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'open paint' in query:
            codePath = 'A:\\Windows\\system32\\mspaint.exe'
            os.startfile(codePath)

        elif 'show my time table for tomorrow' in query:
            webbrowser.open("https:\\apps.skolaro.com")

        elif 'thank you' in query:
            speak("My Pleasure!")

        elif 'I am Anvit' in query:
            speak("Oh! Anvit, Vedant's Brother! How may I help you?")

        elif 'I am Vivek' in query:
            speak("Oh! Vivek, Vedant's Father! How may I help you sir?")

        elif 'I am Aparna' in query:
            speak("Oh! Aparna, Vedant's Mother! How may I help you mam?")

        elif 'hello' in query:
            speak("Hey! Glad to hear you! How may I help you?")

        elif 'bye' in query:
            speak("Bye! See you soon")

        elif 'open Notepad ' in query:
            codePath = 'A:\\Windows\\System32\\notepad.exe'
            os.startfile(codePath)
