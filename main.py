from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
from dotenv import load_dotenv
import os


app = Flask(__name__)
CORS(app)
load_dotenv()
GOOGLE_API_KEY = os.getenv('API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/', methods=['GET'])
def home():
    return "Hello World"


@app.route('/generate', methods=['POST'])
def generate():
    message = request.json['message']
    response = model.generate_content(message)
    # print(response.text)
    return jsonify({"response": response.text})



if __name__ == '__main__':
    app.run(debug=True)
    