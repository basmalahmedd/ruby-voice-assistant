import speech_recognition as sr 
import pyttsx3
import pywhatkit
import pyjokes
import requests
from datetime import datetime, timedelta

# CONFIGURATION
API_KEY = "8419dabc35767ad4a21686a99639cfb4"  

def get_city_from_ip():
    try:
        ip_info = requests.get("https://ipinfo.io").json()
        return ip_info.get("city", "Cairo")
    except:
        return "Cairo"

recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Voice
voices = engine.getProperty('voices')
for voice in voices:
    if "female" in voice.name.lower() or "zira" in voice.name.lower():
        engine.setProperty('voice', voice.id)
        break

engine.setProperty('rate', 150)  # speed

# TTS Function
def speak(text):
    print("Ruby:", text)
    engine.say(text)
    engine.runAndWait()

# STT Function
def listen(timeout=5, phrase_time_limit=8):
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("🎤 Listening...")
        try:
            audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
        except sr.WaitTimeoutError:
            return ""
    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        speak("Could not request results. Please check your internet.")
        return ""

# Get Weather Info
def get_weather():
    city = get_city_from_ip()
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()
        if data["cod"] != 200:
            return f"Sorry, I couldn't fetch the weather for {city}."
        temp = data["main"]["temp"]
        description = data["weather"][0]["description"]
        return f"The weather in {city} is {description} with a temperature of {temp} degrees Celsius."
    except:
        return "Sorry, something went wrong while getting the weather."

# Respond to Commands
def respond_to_command(command):
    if "your name" in command:
        speak("My name is Ruby, your voice assistant.")
    elif "time" in command:
        now = datetime.now()
        speak(f"The time is {now.strftime('%I:%M %p')}")
    elif "joke" in command:
        speak(pyjokes.get_joke())
    elif "search for" in command:
        search_term = command.replace("search for", "").strip()
        speak(f"Searching for {search_term} on Google")
        pywhatkit.search(search_term)
    elif "play" in command:
        song = command.replace("play", "").strip()
        speak(f"Playing {song} on YouTube")
        pywhatkit.playonyt(song)
    elif "weather" in command:
        speak(get_weather())
    elif "exit" in command or "quit" in command:
        speak("Goodbye!")
        return False
    else:
        speak("Sorry, I didn’t understand that.")
    return True


def main():
    speak("Ruby is listening. Say 'Ruby' to wake me up.")
    while True:
        print("🔇 Waiting for wake word: Ruby...")
        wake_input = listen(timeout=10, phrase_time_limit=5)
        if "ruby" in wake_input:
            speak("Yes? I’m awake for five minutes.")
            awake_until = datetime.now() + timedelta(minutes=5)

            while datetime.now() < awake_until:
                print("🟢 Ruby is active. Say a command...")
                user_command = listen()
                if user_command == "":
                    continue
                if not respond_to_command(user_command):
                    return
            speak("Going back to sleep.")

if __name__ == "__main__":
    main()
