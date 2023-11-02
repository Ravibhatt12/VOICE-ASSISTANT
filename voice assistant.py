import speech_recognition as sr
import pyttsx3

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize voice commands
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print("You said:", command)
            return command
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
            return ""
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return ""

# Main loop
while True:
    command = listen()
    
    if "hello" in command:
        speak("Hello! How can I help you?")
    
    elif "goodbye" in command:
        speak("Goodbye! Have a great day!")
        break