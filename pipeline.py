import wave, sys, pyaudio, time
import whisper
from ollama import chat
import pyttsx3

def listen():
    try:
            CHUNK = 1024
            FORMAT = pyaudio.paInt16
            CHANNELS = 1
            RATE = 16000
            RECORD_SECONDS = 5

            with wave.open('output.wav', 'wb') as wf:
                p = pyaudio.PyAudio()
                wf.setnchannels(CHANNELS)
                wf.setsampwidth(p.get_sample_size(FORMAT))
                wf.setframerate(RATE)

                stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True)

                print('Recording...')
                for _ in range(0, RATE // CHUNK * RECORD_SECONDS):
                    wf.writeframes(stream.read(CHUNK))
                print('Done')

                stream.close()
                p.terminate()
    except:
        print("Error")

model = whisper.load_model("turbo")
def transcribe():
    try:
        result = model.transcribe("output.wav")
        print(result["text"])
        return (result["text"])
    except:
        print("Error in Transcribing")

def response(text)->str:
    try:
        response = chat(model='qwen2.5:7b',
                        messages=[
                            {"role": "system",
                             "content": "You are JARVIS. Be short and direct."},
                            {"role": "user",
                             "content": text}
                        ])
        print(response.message.content)
        return (response.message.content)
    except:
        print("Error in Response")

def speak(text)-> None:
    try:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    except:
        print("Error in Speaking")

if __name__ == "__main__":
    speak("Initializing JARVIS...")
    print("Initializing JARVIS...")
    while True:
        listen()
        reply=response(transcribe())
        speak(reply)
        time.sleep(5)
