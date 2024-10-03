import pyttsx3
import speech_recognition as sr
from flask import Flask, jsonify, render_template
from debate_logic import debate_logic

app = Flask(__name__)

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Initialize the speech recognizer
recognizer = sr.Recognizer()

# Function to convert AI response to speech
def speak_response(response_text):
    engine.say(response_text)
    engine.runAndWait()

@app.route("/debate_voice", methods=["POST"])
def debate_voice():
    # Get user input from microphone
    user_input = capture_user_input()  # This will listen to the microphone

    # Get AI's counterpoint using the debate logic
    ai_response = debate_logic(user_input)

    # Speak the AI response
    speak_response(ai_response)

    return jsonify({"user_input": user_input, "response": ai_response})

@app.route("/")
def index():
    return render_template("index.html")

def capture_user_input():
    with sr.Microphone() as source:
        print("Listening... Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            user_input = recognizer.recognize_google(audio)
            print(f"User Input: {user_input}")
            return user_input
        except sr.UnknownValueError:
            return "Sorry, I could not understand your speech."
        except sr.RequestError:
            return "Sorry, there was a problem with the speech recognition service."

if __name__ == "__main__":
    app.run(debug=True)
