# twitterApp

twitter api で遊ぶ



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
Status(_api, _json{}, created_at, id, id_str, text, truncated, entities{}, extended_entities{}, metadata{}, source,
       source_url, in_reply_to_status_id, in_reply_to_status_id_str, in_reply_to_user_id, in_reply_to_user_id_str,
       in_reply_to_screen_name, author=User(), user==User(), geo, coordinates, place, contributors, is_quote_status,
       retweet_count, favorite_count, favorited, retweeted, possibly_sensitive, lang)
https://developer.twitter.com/en/docs/twitter-api/v1/tweets/search/api-reference/get-search-tweets
