# twitterApp

twitter api で遊ぶ

## 環境変数
```sh
CONSUMER_KEY
CONSUMER_SECRET
BEARER
ACCESS_TOKEN
ACCESS_TOKEN_SECRET
SLACK_WEBHOOK_URL
QUERY
```

## docker 備忘録
```sh
docker compose up -d --build
docker compose exec python3 bash
# python -m pip install <package>
docker compose down
```

### jupyter-lab server
```sh
docker run -v $PWD/app:/root/opt -w /root/opt -it --rm -p 7777:8888 twitterapp-python3 jupyter-lab --no-browser --ip 0.0.0.0 --allow-root -b localhost
```
http://127.0.0.1:7777

## Docs
### TweetObject
https://developer.twitter.com/en/docs/twitter-api/v1/tweets/search/api-reference/get-search-tweets

## heroku
manual deploy