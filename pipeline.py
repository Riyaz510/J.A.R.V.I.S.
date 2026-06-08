import wave, pyaudio, time
import whisper
from ollama import chat
import pyttsx3
import speech_recognition as sr
import webbrowser
def listen():
    try:
            # CHUNK = 1024
            # FORMAT = pyaudio.paInt16
            # CHANNELS = 1
            # RATE = 16000
            # RECORD_SECONDS = 5
            #
            # with wave.open('output.wav', 'wb') as wf:
            #     p = pyaudio.PyAudio()
            #     wf.setnchannels(CHANNELS)
            #     wf.setsampwidth(p.get_sample_size(FORMAT))
            #     wf.setframerate(RATE)
            #
            #     stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True)
            #
            #     print('Recording...')
            #     for _ in range(0, RATE // CHUNK * RECORD_SECONDS):
            #         wf.writeframes(stream.read(CHUNK))
            #     print('Done')
            #
            #     stream.close()
            #     p.terminate()

            r = sr.Recognizer()
            # recognize speech using Sphinx
            try:
                with sr.Microphone() as source:
                    print("Listening for Jarvis..!")
                    audio = r.listen(source)
                word = (r.recognize_google(audio))
                print(word)
                if word.lower() == "jarvis" or "friday":
                    speak("Jarvis Active..")
                    with sr.Microphone() as source:
                        print("<- Listening for command ->!")
                        audio = r.listen(source)
                        cmd = (r.recognize_google(audio))

                        processcmd(cmd)
            except Exception as e:
                print(f"Jarvis Error {e}")
    except Exception as e:
        print(f"Listening Error {e}")

def processcmd(cmd):
    print(f"Processing command: {cmd}")
    if "open google" or "google" in cmd.lower():
        webbrowser.open("https://www.google.com")
    elif "open youtube" or "youtube" in cmd.lower():
        webbrowser.open("https://www.youtube.com")
    elif "open github" or "github" in cmd.lower():
        webbrowser.open("https://github.com/Riyaz510")
    elif "open claude" or "claude" in cmd.lower():
        webbrowser.open("https://claude.ai/new")
    else:
        response(cmd)

def response(text)->None:
    try:
        response = chat(model='qwen2.5:7b',
                        messages=[
                            {"role": "system",
                             "content": "You are JARVIS. Be short and direct."},
                            {"role": "user",
                             "content": text}
                        ])
        print(response.message.content)
        return response.message.content
    except Exception as e:
        print(f"Response Error {e}")

def speak(text)-> None:
    try:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"Speak Error {e}")


if __name__ == "__main__":
    speak("Initializing JARVIS...")
    print("Initializing JARVIS...")
    listen()