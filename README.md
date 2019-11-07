# なにこれ
ポートフォリオだよ、ここにデプロイされるよ。
https://portfolio-256304.appspot.com

## 環境
GAE + GCS + Python3/Flask + Vuejs
CIはCircleCI

FlaskでAPIを送信して、Vuejsで結果を表示する。

Vuejs側で叩かれたファイルやディレクトリをGCSから探し出して表示している。

## ローカルで動かすには
```shell
docker build -t portfolio .
docker run -itd -p 8080:8080 --rm --name portfolio portfolio
docker exec portfolio gunicorn -b :8080 backend.main:app
```

## circleciのデバッグ
https://circleci.com/docs/ja/2.0/local-cli/