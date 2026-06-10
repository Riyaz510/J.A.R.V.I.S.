# J.A.R.V.I.S. - AI Voice Assistant

J.A.R.V.I.S. is a Python-based desktop virtual assistant designed to perform basic tasks, answer questions using a local Large Language Model (LLM), and provide information upon voice command. It uses speech recognition to listen for its wake word and executes commands or converses with the user using text-to-speech.

## Features

- **Wake Word Detection:** Constantly listens for the wake words ("Jarvis" or "Friday") to activate.
- **Voice Commands:** Responds to voice commands and provides spoken feedback.
- **Web Navigation:** Can open popular websites such as Google, YouTube, GitHub, and Claude.
- **Formula 1 Integration:** Fetches F1 driver information (Full Name, Team Name) based on their driver number using the OpenF1 API.
- **Local LLM Integration:** Uses [Ollama](https://ollama.com/) to process general queries and converse with the user locally, specifically using the `qwen2.5:7b` model. No cloud processing is required for the conversational AI part.

## Prerequisites

To run this project, you will need the following installed on your system:

- **Python 3.x**
- **Microphone:** Required for voice input.
- **Speaker/Headphones:** Required for audio output.
- **Ollama:** You must have Ollama installed and the `qwen2.5:7b` model downloaded on your machine to use the AI chat features.

### Python Libraries

You will need to install the following Python packages:

- `SpeechRecognition` - For processing audio from the microphone and converting it to text.
- `pyttsx3` - For offline text-to-speech conversion.
- `requests` - For making HTTP requests to external APIs (e.g., OpenF1).
- `ollama` - The official Python client for Ollama.
- `PyAudio` - A dependency for `SpeechRecognition` to access the microphone.

## Installation

1. **Clone or download the repository:**
   Navigate to the project directory:
   ```bash
   cd Jarvis
   ```

2. **Set up a Virtual Environment (Optional but recommended):**
   ```bash
   python -m venv env
   # Activate the virtual environment
   # On Windows:
   .\env\Scripts\activate
   # On macOS/Linux:
   source env/bin/activate
   ```

3. **Install dependencies:**
   Install the core packages listed in [requirements.txt]:
   ```bash
   pip install -r requirements.txt
   ```

4. **Setup Ollama:**
   - Install Ollama from [https://ollama.com/](https://ollama.com/)
   - Pull the Qwen 2.5 7B model by running this command in your terminal:
     ```bash
     ollama pull qwen2.5:7b
     ```

## Usage

The project's primary entry point is [main.py].

Run the assistant:
```bash
python main.py
```

### How to interact:
1. Wait for the console to say `Listening for Jarvis..!`.
2. Say **"Jarvis"** or **"Friday"**.
3. Once activated (you will hear "Jarvis Active.."), speak your command.
   - *Example commands:*
     - "Open Google"
     - "Open YouTube"
     - "F1" (It will then ask for a driver number)
     - "What is the capital of France?" (This will be routed to the local LLM)

## Project Structure

```text
Jarvis/
├── main.py             # Primary assistant script with all features
├── requirements.txt    # Python dependencies
└── env/                # Python virtual environment (if created)
```

## Troubleshooting

- **`PyAudio` installation errors:** On Windows, if `pip install pyaudio` fails, you might need to install it via a `.whl` file from Christoph Gohlke's repository or use `pipwin` (`pip install pipwin` then `pipwin install pyaudio`). On Linux, you may need `portaudio19-dev` (`sudo apt install portaudio19-dev python3-pyaudio`).
   *(Note: See [Troubleshooting](#troubleshooting) if you run into issues installing PyAudio.)*
- **Microphone not detected:** Ensure your default recording device is set correctly in your OS settings and that Python has microphone permissions.
- **LLM taking too long or failing:** Ensure Ollama is running in the background and the `qwen2.5:7b` model has been downloaded successfully.
- **Speech Recognition Unknown Value Error:** This means the Speech Recognition API couldn't understand the audio. Try speaking closer to the microphone or reducing background noise.
