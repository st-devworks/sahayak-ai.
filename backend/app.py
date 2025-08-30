import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from dotenv import load_dotenv
from groq import Groq

# Load environment variables from root .env
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))

print("GROQ API KEY:", os.getenv("GROQ_API_KEY"))

app = Flask(__name__, static_folder="static", template_folder="templates")
CORS(app)

# Initialize Groq client (uses GROQ_API_KEY from environment)
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/api/ask", methods=["POST"])
def ask():
    try:
        data = request.get_json(force=True)
        query = (data or {}).get("query", "").strip()
        if not query:
            return jsonify({"error": "Missing 'query'"}), 400

        # Call Groq Chat Completions API
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",  # Groq fast & free model
            messages=[
                {"role": "system", "content": "You are Sahayak AI, a helpful Indian multilingual assistant."},
                {"role": "user", "content": query},
            ],
        )

        reply = completion.choices[0].message.content
        return jsonify({"reply": reply})

    except Exception as e:
        print("Error:", e)
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="127.0.0.1", port=port, debug=True)
