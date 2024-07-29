import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import os
import time
import subprocess

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query.lower()

def greet():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Boss!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Boss!")
    else:
        speak("Good Evening Boss!")
    speak("I am your desktop assistant. How can I help you today?")

def open_notepad():
    subprocess.Popen(['notepad.exe'])

def open_calculator():
    subprocess.Popen(['calc.exe'])

def set_reminder(reminder_time, message):
    current_time = datetime.datetime.now()
    target_time = datetime.datetime.strptime(reminder_time, "%H:%M")
    delta = target_time - current_time

    if delta.total_seconds() > 0:
        speak(f"Setting a reminder for {reminder_time}.")
        time.sleep(delta.total_seconds())
        speak(f"Reminder: {message}")
    else:
        speak("The specified time has already passed.")

def main():
    greet()
    while True:
        query = take_command()

        if 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'play music' in query:
            music_dir = 'path/to/your/music/directory'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'open notepad' in query:
            open_notepad()

        elif 'open calculator' in query:
            open_calculator()

        elif 'set reminder' in query:
            speak("At what time would you like to set the reminder?")
            reminder_time = take_command()  # Example: "14:30"
            speak("What is the reminder message?")
            message = take_command()
            set_reminder(reminder_time, message)

        elif 'exit' in query or 'stop' in query:
            speak("Goodbye!")
            break

if __name__ == "__main__":
    main()
