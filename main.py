import speech_recognition as sr
import pyttsx3
import webbrowser
import requests
from ollama import chat

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
    else:
        try:
            response = chat(model='qwen2.5:7b',
                            messages=[
                                {"role": "system",
                                 "content": "You are JARVIS, a virtual assistant like Alexa and Google Cloud. Be short and direct."},
                                {"role": "user",
                                 "content": cmd}
                            ])
            output=response.message.content
            print(output)
            speak(output)
        except Exception as e:
            print(f"Response Error {e}")

if __name__ == '__main__':
    speak("Initializing JARVIS.....")
    while True:
        r = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                print("Listening for Jarvis..!")
                audio = r.listen(source)
            word=(r.recognize_google(audio))
            print(word)
            if "jarvis" in word.lower() or "friday" in word.lower():
                speak(f"{word} Active..")
                while True:
                    try:
                        with sr.Microphone() as source:
                            print("<- Listening for command ->!")
                            audio = r.listen(source)
                            cmd=(r.recognize_google(audio))
                            if "exit" in cmd.lower():
                                speak("Jarvis says Adios..!")
                                break
                            else:
                                processcmd(cmd)
                    except :
                        print("Error in understanding the command,say again")
        except sr.UnknownValueError:
            print("Jarvis could not understand audio")
        except sr.RequestError as e:
            print("Jarvis error; {0}".format(e))