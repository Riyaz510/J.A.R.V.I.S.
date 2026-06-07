import wave, sys, pyaudio
import whisper
from ollama import chat
import pyttsx3

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1 if sys.platform == 'darwin' else 2
RATE = 44100
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


model = whisper.load_model("turbo")
result = model.transcribe("output.wav")
print(result["text"])

response = chat(model='qwen2.5:7b',
                messages=[
                    {"role": "system",
                     "content": "You are JARVIS. Be short and direct."},
                    {"role": "user",
                     "content": result["text"]}
                ])
print(response.message.content)

pyttsx3.speak(response.message.content)