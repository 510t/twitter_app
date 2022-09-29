# twitterApp

twitter api で遊ぶ

## jupyter-lab server
```sh
docker run -v $PWD/app:/root/opt -w /root/opt -it --rm -p 7777:8888 twitterapp-python3 jupyter-lab --no-browser --ip 0.0.0.0 --allow-root -b localhost
```
http://127.0.0.1:7777
