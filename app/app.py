from dotenv import load_dotenv
import os
from slack_bolt import App
from slack_bolt.adapter.flask import SlackRequestHandler
from slack_sdk import WebClient
from flask import Flask, request, jsonify
import tweepy

load_dotenv()

flask_app = Flask(__name__)
app = App()
handler = SlackRequestHandler(app)

@flask_app.route('/', methods=['GET', 'POST'])
def handle_slack_events():
    return handler.handle(request)

@flask_app.route('/index')
def index():
    return "OK"


if __name__ == "__main__":
    flask_app.run(host="0.0.0.0", port=5000, debug=True)
