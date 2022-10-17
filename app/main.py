import math
import sys
import tweepy
from dotenv import load_dotenv
import os
import slackweb
import datetime

load_dotenv()
CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
BEARER = os.getenv('BEARER')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')

SLACK_WEBHOOK_URL = os.getenv('SLACK_WEBHOOK_URL')

QUERY = os.getenv('QUERY')


def convert_status_to_url(status):
    tweet_id = status.id
    user_name = status.user.screen_name
    url = f'https://twitter.com/{user_name}/status/{tweet_id}'
    return url


# 2時間前～1時間前のツイートを取得するクエリ
def create_query_by_time():
    jst = datetime.timezone(datetime.timedelta(hours=+9), 'JST')
    now = datetime.datetime.now(jst)
    year = now.year
    month = now.month
    day = now.day
    hour = now.hour

    until = f'until:{year}-{month}-{day}_{hour - 1}:00:00_JST'
    since = f'since:{year}-{month}-{day}_{hour - 2}:00:00_JST'

    return f'{QUERY} {until} {since}'


def get_tweets_by_query():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)

    query = create_query_by_time()
    tweets = api.search_tweets(q=query, result_type='recent', count=100)
    tweets.reverse()

    return tweets


def post_tweet_to_slack(tweet):
    url = convert_status_to_url(tweet)
    slack = slackweb.Slack(url=SLACK_WEBHOOK_URL)
    slack.notify(text=url)


def main():
    tweets = get_tweets_by_query()
    for tweet in tweets:
        post_tweet_to_slack(tweet)


if __name__ == "__main__":
    main()
