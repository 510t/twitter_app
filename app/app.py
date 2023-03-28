from dotenv import load_dotenv
import os
from slack_bolt import App
from slack_bolt.adapter.flask import SlackRequestHandler
from slack_sdk import WebClient
from flask import Flask, request, jsonify, send_file, make_response
import tweepy
import csv

# env var
load_dotenv()
CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
BEARER = os.getenv('BEARER')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')
SLACK_WEBHOOK_URL = os.getenv('SLACK_WEBHOOK_URL')
SLACK_BOT_TOKEN = os.getenv('SLACK_BOT_TOKEN')

# tweepy api
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
LIST_USER_MAX_COUNT = 3000

# flask
flask_app = Flask(__name__)

# slack
app = App()
handler = SlackRequestHandler(app)

def list_id_to_urls(list_id):
    users = api.get_list_members(list_id=list_id, count=LIST_USER_MAX_COUNT)

    pixiv_urls = []
    for user in users:
        entities = user.entities
        if 'url' in entities:
            urls = entities['url']['urls']
            if len(urls) > 0:
                for url_dict in urls:
                    url = url_dict['expanded_url']
                    if not url == None:
                        if "pixiv" in url:
                            pixiv_urls.append(url)

        if 'description' in entities:
            urls = entities['description']['urls']
            if len(urls) > 0:
                for url_dict in urls:
                    url = url_dict['expanded_url']
                    if not url == None:
                        if "pixiv" in url:
                            pixiv_urls.append(url)

    return pixiv_urls

@flask_app.route('/', methods=['GET', 'POST'])
def handle_slack_events():
    return handler.handle(request)

@flask_app.route('/index')
def index():
    return "OK"

@flask_app.route('/pixiv', methods=['GET', 'POST'])
def pixiv():
    if request.method == 'POST':
        list_id = request.form['list_id']

        # list_id から csv をつくる処理
        urls = list_id_to_urls(list_id)
        with open('my_list.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(urls)
        # csv をダウンロードする
        with open('my_list.csv', 'r', encoding='utf-8') as f:
            csv_data = f.read()

        # ダウンロード用のレスポンスを作成する
        response = make_response(csv_data)
        response.headers["Content-Disposition"] = "attachment; filename=data.csv"
        response.headers["Content-type"] = "text/csv"

        return response
    else:
        return '''
            <form method="post">
                <label for="list_id">Enter list_id:</label>
                <input type="text" name="list_id" id="list_id">
                <input type="submit" value="Submit">
            </form>
        '''


if __name__ == "__main__":
    flask_app.run(host="0.0.0.0", port=5000, debug=True)
