import speech_recognition as sr
import pyttsx3
import webbrowser
import requests

recognizer = sr.Recognizer()

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def processcmd(cmd):
    print(f"Processing command: {cmd}")
    if "google" in cmd.lower():
        webbrowser.open("https://www.google.com")
    elif "youtube" in cmd.lower():
        webbrowser.open("https://www.youtube.com")
    elif "github" in cmd.lower():
        webbrowser.open("https://github.com/Riyaz510")
    elif "claude" in cmd.lower():
        webbrowser.open("https://claude.ai/new")
    elif "f1" in cmd.lower():
        try:
            speak("Tell me the driver number")

            with sr.Microphone() as source:
                print("-- Waiting for Driver Number --")
                audio = recognizer.listen(source)

            num = recognizer.recognize_google(audio)

            print("Driver Number:", num)

            url = f"https://api.openf1.org/v1/drivers?driver_number={num}&session_key=9158"

            response = requests.get(url)
            data = response.json()

            if not data:
                speak("Driver not found")
                return

            driver_number = data[0]["driver_number"]
            full_name = data[0]["full_name"]
            team_name = data[0]["team_name"]

            speak(
                f"Driver Number {driver_number}. "
                f"Full Name {full_name}. "
                f"Team Name {team_name}."
            )

        except Exception as e:
            print("Error:", e)
            speak("Sorry, I could not get the driver information.")

if __name__ == '__main__':
    speak("Initializing JARVIS.....")
    while True:
        r = sr.Recognizer()
        # recognize speech using Sphinx
        try:
            with sr.Microphone() as source:
                print("Listening for Jarvis..!")
                audio = r.listen(source)
            word=(r.recognize_google(audio))
            print(word)
            if "jarvis" in word.lower() or "friday" in word.lower():
                speak("Jarvis Active..")
                with sr.Microphone() as source:
                    print("<- Listening for command ->!")
                    audio = r.listen(source)
                    cmd=(r.recognize_google(audio))

                    processcmd(cmd)

        except sr.UnknownValueError:
            print("Sphinx could not understand audio")
        except sr.RequestError as e:
            print("Sphinx error; {0}".format(e))