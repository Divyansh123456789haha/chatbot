from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import requests
from dotenv import load_dotenv
from db import get_db_connection

load_dotenv()

app = Flask(__name__)
CORS(app)

# Load API credentials
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_URL = "enter your groq api url here"

# Database connection
conn, cur = get_db_connection()

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "").lower()

    # Basic keyword detection
    style = None
    if "street" in user_input:
        style = "street style"
    elif "polo" in user_input or "classy" in user_input:
        style = "classy polo"

    # Query DB
    if style:
        cur.execute("SELECT * FROM tshirts WHERE fit = %s LIMIT 3", (style,))
        products = cur.fetchall()
        product_list = "\n".join([f"- {p['name']} | ₹{p['cost']}" for p in products])
        product_text = f"Here are some {style} options:\n{product_list}"
    else:
        product_text = ""

    # AI Response
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama3-70b-8192",
        "messages": [
            {"role": "system", "content": "You're a friendly style expert at DarkCoal. Help users with suggestions and product advice."},
            {"role": "user", "content": user_input}
        ]
    }

    response = requests.post(GROQ_API_URL, headers=headers, json=payload)
    data = response.json()

    try:
        reply = data["choices"][0]["message"]["content"]
    except (KeyError, IndexError):
        reply = "Sorry, I couldn't generate a response right now."

    return jsonify({"response": product_text + "\n\n" + reply})

@app.route("/test-db")
def test_db():
    cur.execute("SELECT * FROM tshirts LIMIT 1;")
    return jsonify(cur.fetchone())

if __name__ == "__main__":
    app.run(debug=True)
