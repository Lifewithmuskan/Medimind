# from flask import Flask, request, jsonify,send_from_directory
# from flask_cors import CORS
# import requests
# import os
# from dotenv import load_dotenv


# # Load environment variables
# load_dotenv()

# # app = Flask(__name__)
# app = Flask(__name__, static_folder='../medimind-frontend', template_folder='../medimind-frontend')
# CORS(app)

# GROQ_API_KEY = os.getenv("GROQ_API_KEY")
# GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

# conversation_state = {}
# @app.route('/')
# def serve_index():
#     return send_from_directory(app.template_folder, 'index.html')

# @app.route('/<path:path>')
# def serve_static(path):
#     return send_from_directory(app.static_folder, path)

# # @app.route("/", methods=["GET"])
# # def home():
# #     return "Welcome to MediMind! Your AI medical assistant."
# @app.route("/chat", methods=["POST"])
# # def chat():
# #     data = request.json
# #     messages = data.get("messages", [])

# #     payload = {
# #         "model": "llama3-8b-8192",
# #         "messages": messages,
# #         "temperature": 0.7
# #     }

# #     headers = {
# #         "Authorization": f"Bearer {GROQ_API_KEY}"
# #     }

# #     try:
# #         response = requests.post(GROQ_API_URL, json=payload, headers=headers)
# #         response.raise_for_status()
# #         result = response.json()
# #         reply = result['choices'][0]['message']['content']
# #         return jsonify({"reply": reply})
# #     except Exception as e:
# #         print("Error:", e)
# #         if hasattr(e, 'response'):
# #             print("Response:", e.response.text)
# #         return jsonify({"error": str(e)}), 500
# @app.route("/chat", methods=["POST"])
# def chat():
#     data = request.json
#     messages = data.get("messages", [])

#     payload = {
#         "model": "llama3-8b-8192",
#         "messages": messages,
#         "temperature": 0.7
#     }

#     headers = {
#         "Authorization": f"Bearer {GROQ_API_KEY}"
#     }

#     print("Payload:", payload)  # Debug
#     print("Headers:", headers)  # Debug

#     try:
#         response = requests.post(GROQ_API_URL, json=payload, headers=headers)
#         response.raise_for_status()
#         result = response.json()
#         print("Groq response:", result)  # Debug
#         reply = result['choices'][0]['message']['content']
#         return jsonify({"reply": reply})
#     except Exception as e:
#         print("Error:", e)
#         if hasattr(e, 'response'):
#             print("Groq API Response:", e.response.text)  # ✨ This is the most useful part
#         return jsonify({"error": str(e)}), 500


# def get_next_question(step, user_message):
#     # Define the conversation flow based on steps
#     if step == 0:
#         return "Can you tell me more about your stomach ache? Is it: * Sharp * Dull * Crampy?"
#     elif step == 1:
#         if "crampy" in user_message:
#             return "Is the crampy pain constant, or does it come and go?"
#         elif "sharp" in user_message or "dull" in user_message:
#             return "Is the pain located in a specific area of your stomach?"
#         else:
#             return "Can you provide more details about your pain?"
#     elif step == 2:
#         if "comes and goes" in user_message:
#             return "Have you experienced any bloating, nausea, or changes in your bowel movements?"
#         else:
#             return "Is there anything that makes the pain better or worse?"
#     elif step == 3:
#         return "Have you been under stress or eaten anything spicy recently?"
#     else:
#         return "Can you provide more details about your symptoms?"

# if __name__ == "__main__":
#     app.run(debug=True)  

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import requests
import os

# Directly using the API Key here
GROQ_API_KEY = "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"
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

app = Flask(__name__, static_folder='../medimind-frontend', template_folder='../medimind-frontend')
CORS(app)

conversation_state = {}

@app.route('/')
def serve_index():
    return send_from_directory(app.template_folder, 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(app.static_folder, path)

@app.route("/chat", methods=["POST"])
# def chat():
#     data = request.json
#     messages = data.get("messages", [])

#     payload = {
#         "model": "llama3-8b-8192",  # The model you're using
#         "messages": messages,
#         "temperature": 0.7  # Adjust temperature for more randomness (0.0-1.0)
#     }

#     headers = {
#         "Authorization": f"Bearer {GROQ_API_KEY}"
#     }

#     print("Payload:", payload)  # Debugging output for the payload
#     print("Headers:", headers)  # Debugging output for the headers

#     try:
#         response = requests.post(GROQ_API_URL, json=payload, headers=headers)
#         response.raise_for_status()
#         result = response.json()
#         print("Groq response:", result)  # Debugging output for the API response
#         reply = result['choices'][0]['message']['content']
#         return jsonify({"reply": reply})
#     except Exception as e:
#         print("Error:", e)
#         if hasattr(e, 'response'):
#             print("Groq API Response:", e.response.text)  # This is useful for debugging
#         return jsonify({"error": str(e)}), 500
@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    messages = data.get("messages", [])

    payload = {
        "model": "llama3-8b-8192",  # The model you're using
        "messages": messages,
        "temperature": 0.7  # Adjust temperature for more randomness (0.0-1.0)
    }

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}"
    }

    print("Payload:", payload)  # Debugging output for the payload
    print("Headers:", headers)  # Debugging output for the headers

    try:
        response = requests.post(GROQ_API_URL, json=payload, headers=headers)
        response.raise_for_status()
        
        # Debugging: Print the status code and response content
        print("API Status Code:", response.status_code)
        print("API Response:", response.text)

        result = response.json()
        print("Groq response:", result)  # Debugging output for the API response

        # Check if the response is valid and contains the expected content
        if 'choices' in result and len(result['choices']) > 0:
            reply = result['choices'][0]['message']['content']
            return jsonify({"reply": reply})
        else:
            return jsonify({"error": "Unexpected API response format"}), 500
    except Exception as e:
        print("Error:", e)
        if hasattr(e, 'response'):
            print("Groq API Response:", e.response.text)  # This is useful for debugging
        return jsonify({"error": str(e)}), 500

def get_next_question(step, user_message):
    if step == 0:
        
        return "Can you tell me more about your stomach ache? Is it: * Sharp * Dull * Crampy?"
    elif step == 1:
        if "crampy" in user_message:
            return "Is the crampy pain constant, or does it come and go?"
        elif "sharp" in user_message or "dull" in user_message:
            return "Is the pain located in a specific area of your stomach?"
        else:
            return "Can you provide more details about your pain?"
    elif step == 2:
        if "comes and goes" in user_message:
            return "Have you experienced any bloating, nausea, or changes in your bowel movements?"
        else:
            return "Is there anything that makes the pain better or worse?"
    elif step == 3:
        return "Have you been under stress or eaten anything spicy recently?"
    else:
        return "Can you provide more details about your symptoms?"

if __name__ == "__main__":
    app.run(debug=True)
