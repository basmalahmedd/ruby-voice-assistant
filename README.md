# 🎙️ Ruby – Your Personal Voice Assistant

**Ruby** is a real-time Python voice assistant that brings smart features to your desktop. Just say "**Ruby**" to activate her, and she’ll help you with jokes, weather updates, Google searches, music, and more—all hands-free!

---

## 🚀 Features

- 🔊 **Wake Word Activation**: Say "Ruby" to start
- 🗣️ **Speech Recognition**: Powered by `speech_recognition`
- ⏳ **5-Minute Active Window**: After wake word
- 🌦️ **Weather Updates**: Get weather via `wttr.in` 
- 🎵 **Play YouTube Songs**: Just ask for your favorite track
- 🔍 **Google Search**: Quick answers to your questions
- 😂 **Jokes**: Lighten the mood anytime
- 🕒 **Current Time**: Ask for the time
- ❌ **Exit Command**: Say “exit” to stop Ruby

---

## 🛠️ Installation

1. **Install dependencies:**
    ```bash
    pip install SpeechRecognition pyttsx3 pywhatkit pyjokes requests pyaudio
    ```

2. **If you get a `pyaudio` error on Windows:**
    ```bash
    pip install pipwin
    pipwin install pyaudio
    ```

---

## ▶️ Usage

Start Ruby with:
```bash
python ruby_assistant.py
```

---


## 🌦️ Weather Customization

Ruby fetches the current weather in **Cairo** using:
```python
url = "https://wttr.in/Cairo?format=3"
```
To use your own city, just replace `"Cairo"` with your city name.

---

## 🧰 Built With

- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [pyttsx3](https://pypi.org/project/pyttsx3/)
- [pywhatkit](https://github.com/Ankit404butfound/PyWhatKit)
- [pyjokes](https://pypi.org/project/pyjokes/)
- [wttr.in](https://wttr.in)

---

## 📜 License

This project is open-source and licensed under the [MIT License](LICENSE).

---
