import speech_recognition as sr
import time

class Listener:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.offline_count = 0
        self.max_retries = 3

    def listen(self):
        with sr.Microphone() as source:
            print("Listening...")
            try:
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=5)
            except sr.WaitTimeoutError:
                print("No speech detected")
                return ""

        try:
            command = self.recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")
            self.offline_count = 0  # Reset counter on successful recognition
            return command
            
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand.")
            return ""
            
        except sr.RequestError:
            self.offline_count += 1
            if self.offline_count >= self.max_retries:
                print("Network issues detected. Please check your internet connection.")
                time.sleep(2)  # Prevent too rapid retries
                self.offline_count = 0  # Reset counter
            return ""
            
        except Exception as e:
            print(f"Error during speech recognition: {e}")
            return ""
