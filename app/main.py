import math
import sys
import tweepy
from dotenv import load_dotenv
import os
import slackweb

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


def get_tweets_by_query():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)

    query = QUERY
    tweets = api.search_tweets(q=query, result_type='recent')
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
