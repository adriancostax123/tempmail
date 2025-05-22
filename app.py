
from flask import Flask, render_template, jsonify, request
import requests
import random
import string

app = Flask(__name__)

DOMAINS = ["1secmail.com", "1secmail.net", "1secmail.org"]

def generate_random_email():
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    domain = random.choice(DOMAINS)
    return username, domain

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate_email")
def generate_email():
    user, domain = generate_random_email()
    email = f"{user}@{domain}"
    return jsonify({"email": email, "login": user, "domain": domain})

@app.route("/get_messages")
def get_messages():
    login = request.args.get("login")
    domain = request.args.get("domain")
    url = f"https://www.1secmail.com/api/v1/?action=getMessages&login={login}&domain={domain}"
    resp = requests.get(url)
    return jsonify(resp.json())

@app.route("/read_message")
def read_message():
    login = request.args.get("login")
    domain = request.args.get("domain")
    message_id = request.args.get("id")
    url = f"https://www.1secmail.com/api/v1/?action=readMessage&login={login}&domain={domain}&id={message_id}"
    resp = requests.get(url)
    return jsonify(resp.json())

if __name__ == "__main__":
    app.run(debug=True)
