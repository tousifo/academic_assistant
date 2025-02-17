import pyttsx3

class Speaker:
    def __init__(self):
        self.engine = pyttsx3.init()
        # Try to use espeak driver directly
        try:
            self.engine.setProperty('driver', 'espeak')
            # Reduce verbosity of underlying drivers
            self.engine.setProperty('debug', False)
        except:
            pass
        
    def speak(self, text):
        print(f"Assistant: {text}")
        try:
            self.engine.say(text)
            self.engine.runAndWait()
        except Exception as e:
            print(f"Speech error: {e}")
