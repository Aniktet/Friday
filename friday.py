import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pyaudio

print("Initializing Friday")



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    

    if hour>=0 and hour<12:
        print("Good Morning Boss...")
        speak("Good Morning Boss...")

    elif hour>=12 and hour<18:
        print("Good Afternoon Boss...")
        speak("Good Afternoon Boss...")

    else:
        print("Good Evening Boss...")
        speak("Good Evening Boss...")

    #speak("How may I help you?")



def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Please say that again")
        speak("Please say that again")
        query = None
    return query

      



speak("Initializing Friday.....")
wishMe()
query = takeCommand()

if 'wikipedia' in query.lower():
    print("Seraching Wikipedia....")
    speak("Searching Wikipedia....")
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences =2)
    print(results)
    speak(results)

elif 'open youtube' in query.lower():
    url = "youtube.com"
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    print("Opening YouTube")
    speak("Opening YouTube....")
    webbrowser.get(chrome_path).open(url)

elif 'open google' in query.lower():
    url = "google.com"
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    print("Opening Google")
    speak("Opening Google...")
    webbrowser.get(chrome_path).open(url)

elif 'the time' in query.lower():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    print(strTime)
    speak(f"Sir the time is{strTime}")

elif 'open pubg' in query.lower():
    pubgPath = "D:\\program files\\txgameassistant\\appmarket\\AppMarket"
    print("Opening Pubg")
    speak("Opening Pubg....")
    os.startfile(pubgPath)

elif 'open spotify' in query.lower():
    spotifyPath = "C:\\Users\\DHINGRA\\AppData\\Roaming\\Spotify\\Spotify"
    print("Opening Spotify")
    speak("Opening Spotify.....")
    os.startfile(spotifyPath)


elif 'open steam' in query.lower():
    steam_path = "D:\\New folder\\steam"
    print("Opening Steam.....")
    speak("Opening Steam....")
    os.startfile(steam_path)

elif 'open code' in query.lower():
    vs_path = "C:\\Users\\DHINGRA\\AppData\\Local\\Programs\\Microsoft VS Code\\Code"
    print("Opening Code.....")
    speak("Opening Code....")
    os.startfile(vs_path)





