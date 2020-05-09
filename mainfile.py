import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pythoncom
import pyaudio


print("KAREN Akash AI Assistant")
sir = "akash"


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def helloMe():
    hour = int(datetime.datetime.now().hour)


    if hour>=0 and hour<12:
        speak("Good Morning" + sir)

    elif hour>=12 and hour<18:
        speak("Good Afternoon" + sir)

    else:
        speak("Good Evening" + sir)

    speak("I am karen.. AI Assistant . How may I help you ?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-IN')

        print(f"user said : {query}\n")

    except Exception as e:
        print("say that again please")
        query = None
    return query

def sendEmail(to,content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login('sendermail@gmail.com', 'senderpassword')
    server.sendmail('recivermail@gmail.com', to, content)
    server.close()

def main():
    speak("starting.. karen.. Akash AI Assistant...")
    helloMe()
    query = takeCommand()

    if "wikipedia" in query.lower():
        speak("searching wikipedia....")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        print(results)
        speak(results)

    elif 'open google' in query.lower():
        webbrowser.open("google.com")

    elif 'open github' in query.lower():
        webbrowser.open("github.com")

    elif 'open youtube' in query.lower():
        webbrowser.open("youtube.com")

    elif 'open facebook' in query.lower():
        webbrowser.open("facebook.com")

    elif 'open whatsapp web' in query.lower():
        webbrowser.open("web.whatsapp.com")

    elif 'play music' in query.lower():
        songs_dir = "C:\\Users\\user\\Downloads\\Music"
        songs = os.listdir(songs_dir)
        print(songs)
        os.startfile(os.path.join(songs_dir, songs[0]))

    elif 'play video' in query.lower():
        video_dir = "C:\\Users\\user\\Downloads\\Video"
        video = os.listdir(video_dir)
        print(video)
        os.startfile(os.path.join(video_dir, video[0]))

    elif 'time' in query.lower():
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"{sir} the time is {strTime}")

    elif 'email' in query.lower():
        try:
            speak("what should I send ?")
            content = takeCommand()
            to = "recivermail@gmail.com"
            sendEmail(to, content)
            speak("Email has been sent successfully")

        except Exception as e:
            print(e)
main()









