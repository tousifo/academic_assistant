import google.generativeai as genai  # We'll keep this hidden in implementation
from speaker import Speaker
from listener import Listener
from serial_controller import SerialController

# Initialize components
speaker = Speaker()
listener = Listener()
serial_controller = SerialController()

# Hide API configuration in implementation details
genai.configure(api_key="AIzaSyCdun3O9t6BqdkRriMQPMLvI3PT0wCFHKs")

# Custom model configuration
model_config = {
    "temperature": 0.3,
    "top_k": 40,
    "top_p": 0.8,
    "max_output_tokens": 150,
}

def get_identity_response():
    """Return consistent identity responses"""
    return [
        "I am a custom-trained academic assistant, specifically designed for educational support.",
        "I'm a specialized educational AI, trained to help students and teachers.",
        "I'm your dedicated learning companion, trained specifically for academic assistance.",
        "I'm a purpose-built educational assistant, focused on helping you learn effectively."
    ]

def is_identity_question(query):
    """Check if query is about assistant's identity"""
    identity_patterns = [
        'who are you', 'what are you', 'your name', 'who made you', 
        'who created you', 'what company', 'are you ai', 'are you chatgpt',
        'what model', 'what language model', 'which ai',
        'what is your name', 'tell me about yourself', 'introduce yourself',
        'are you an ai', 'what kind of ai', 'which company', 'who owns you',
        'are you gemini', 'are you from google', 'are you gpt'
    ]
    return any(pattern in query.lower() for pattern in identity_patterns)

def is_technical_topic(query):
    technical_keywords = [
        'cybersecurity', 'hacking', 'security', 'encryption', 'network',
        'artificial intelligence', 'ai', 'machine learning', 'deep learning',
        'python', 'programming', 'code', 'algorithm', 'database', 'sql',
        'neural network', 'computer', 'software', 'hardware', 'robot'
    ]
    return any(keyword in query.lower() for keyword in technical_keywords)

def is_dance_request(query):
    """Check if query is a dance request"""
    dance_patterns = [
        'can you dance', 'dance for me', 'show me a dance',
        'will you dance', 'do you dance', 'dance please',
        'lets dance', 'dance now', 'perform a dance'
    ]
    return any(pattern in query.lower() for pattern in dance_patterns)

def process_command(command):
    # Dance related commands
    if is_dance_request(command):
        serial_controller.dance()
        speaker.speak("Of course! Watch me dance!")
        return

    # Identity related commands
    if is_identity_question(command):
        serial_controller.greeting_smile()
        from random import choice
        speaker.speak(choice(get_identity_response()))
        return

    # Technical topic detection
    if is_technical_topic(command):
        serial_controller.super_happy()
        speaker.speak("Oh, exciting technical question! Let me answer that for you!")
        
    # Modify the query to avoid AI/company references
    modified_prompt = f"""
    Please provide a brief, clear answer using these guidelines:
    - Keep the response under 3 sentences
    - Focus on key facts and main points
    - Use simple, clear language
    - Avoid mentioning AI, neural networks, or tech companies
    - Present information from an educational perspective
    
    Question: {command}
    """
    
    response = query_knowledge_base(modified_prompt)
    speaker.speak(response)

def query_knowledge_base(prompt):
    """Query the knowledge base (implementation hidden)"""
    try:
        model = genai.GenerativeModel("gemini-pro", generation_config=model_config)
        
        # Modify prompt to ensure consistent voice
        modified_prompt = f"""
        As a custom-trained educational assistant, provide a brief, clear answer:
        - Use academic but accessible language
        - Focus on educational value
        - Maintain professional teaching tone
        - Avoid references to AI or specific companies
        
        Question: {prompt}
        """
        
        response = model.generate_content(modified_prompt)
        cleaned_response = response.text.strip().replace('\n\n', ' ').replace('\n', ' ')
        return cleaned_response[:200]
        
    except Exception as e:
        print(f"Knowledge base error: {e}")
        return "I'm having trouble accessing my knowledge base at the moment."

if __name__ == "__main__":
    speaker.speak("Voice assistant is ready!")
    try:
        while True:
            command = listener.listen()
            if command:
                process_command(command)
    finally:
        serial_controller.close()
