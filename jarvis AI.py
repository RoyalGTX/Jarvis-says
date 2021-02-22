import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am jarvis Sir. how may I help you")


def takecommand():
    # it takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")

    except Exception as e:
        # print(e)

        print("Say that again Please...")
        return "none"
    return query


if __name__ == "__main__":
    wishMe()
    if 1:
        query = takecommand().lower()

        # logic for executing tasks based on query
        if 'Wikipedia ' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to wikipedia")
            speak(results)
            print(results)

        elif 'open google' in query:
            speak("oK Sir opening google.")
            webbrowser.open("www.google.com")

        elif 'open youtube' in query:
            speak("oK Sir opening YouTube.")
            webbrowser.open("www.youtube.com")

        elif 'open stack overflow' in query:
            speak("oK Sir opening stackoverflow  ")
            webbrowser.open("www.stackoverflow.com")

        elif 'what can ' in query:
            speak("i  can open various websites and apps which you use often ")

        elif ' the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strtime}")

        elif 'play music' in query:
            speak('Ok sir, playing music')
            music_dir = "E:\music\songs"
            songs = os.listdir(music_dir)
            print(random.shuffle(songs))
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'open launcher' in query:
            speak('ok sir opening epic games')
            launcherPath = "C:\\Program Files (x86)\\Epic Games\\Launcher\\Portal\\Binaries\\Win32\\EpicGamesLauncher.exe"
            os.startfile(launcherPath)

        elif 'open class' in query:
            speak('ok sir opening zoom')
            zoomPath = "C:\\Users\\ADMIN\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
            os.startfile(zoomPath)

        elif 'open visual studio' in query:
            speak ('ok Sir opening visual studio')
            codePath = "C:\\Users\\ADMIN\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif '  useless jarvis' in query:
            speak("NO! i am not useless ")















