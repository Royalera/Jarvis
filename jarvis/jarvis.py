import speech_recognition as sr
import pyttsx3
import os
import url_checker  # Import the website opener module

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Capture voice input from the microphone."""
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            print("Sorry, I didn't understand.")
            return ""
        except sr.RequestError:
            print("Speech service unavailable.")
            return ""

def execute_command(command):
    """Perform tasks based on the voice command."""
    if "open notepad" in command:
        speak("Opening Notepad")
        os.system("notepad")
    elif "open calculator" in command:
        speak("Opening Calculator")
        os.system("calc")
    elif "open" in command:
        website = command.replace("open", "").strip()
        if website:
            speak(f"Checking for {website}")
            if url_checker.open_url(website):
                speak(f"Opening {website}")
            else:
                speak("Website not found.")
        else:
            speak("Please specify a website.")
    elif "exit" in command or "quit" in command:
        speak("Goodbye!")
        exit()
    else:
        speak("I didn't understand that command.")

if __name__ == "__main__":
    speak("Hello, I am Jarvis. How can I assist you?")
    while True:
        user_command = listen()
        if user_command:
            execute_command(user_command)
