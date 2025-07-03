# 🎙️ Ruby – Your Personal Voice Assistant

**Ruby** is a real-time Python voice assistant. She listens for the wake word "**Ruby**", stays active for 5 minutes, and supports tasks like telling jokes, checking the weather, searching Google, playing music, and more.

---

## 🚀 Features

- 🔊 **Wake word**: Say "Ruby" to activate
- 🗣️ **Speech recognition** (via `speech_recognition`)
- 🧠 Active for 5 minutes after wake
- 🌤️ **Weather in Cairo** using `wttr.in` (no API key required)
- 🎵 **Play YouTube songs**
- 🔍 **Search Google**
- 😂 **Jokes**
- ⏰ **Current time**
- ❌ Say “exit” to stop

---

## 🛠️ Installation

```bash
pip install SpeechRecognition pyttsx3 pywhatkit pyjokes requests pyaudio
```

If `pyaudio` gives an error on Windows:
```bash
pip install pipwin
pipwin install pyaudio
```

---

## ▶️ Run the Assistant

```bash
python ruby_assistant.py
```

---


## 🌦️ Weather Info

Ruby fetches the current weather in **Cairo** using `wttr.in`:
```python
url = "https://wttr.in/Cairo?format=3"
```

Change `"Cairo"` to your own city name if desired.

---



## 🧰 Powered By

- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [pyttsx3](https://pypi.org/project/pyttsx3/)
- [pywhatkit](https://github.com/Ankit404butfound/PyWhatKit)
- [pyjokes](https://pypi.org/project/pyjokes/)
- [wttr.in](https://wttr.in)

---

## 📜 License

This project is open-source and licensed under the [MIT License](LICENSE).

---
