from dotenv import load_dotenv
load_dotenv()

import os
from slack_bolt import App

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def respond_message():
    json = request.json
    d = {'challenge': json["challenge"]}
    return jsonify(d)


@app.route('/index')
def index():
    return "OK"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
