from flask import Flask, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.0-flash")

@app.route("/")
def home():
    return "NAV AI ONLINE"

@app.route("/ai/ask", methods=["GET"])
def ask_ai():
    question = request.args.get("question")
    if not question:
        return jsonify({"reply": "Question missing"})
    try:
        response = model.generate_content(question)
        answer = response.text
    except Exception as e:
        answer = str(e)
    return jsonify({"reply": answer})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
