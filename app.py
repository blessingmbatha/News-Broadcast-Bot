from flask import Flask, request, abort, redirect, session, url_for

from flask.json import jsonify

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, StickerSendMessage
)
from requests_oauthlib import OAuth2Session
import logging

# This information is obtained upon registration of a new GitHub
client_id = "1657607783"
client_secret = "1437c2fc73ecc30def7400bbc8af76ce"
authorization_base_url = 'https://access.line.me/oauth2/v2.1/authorize'
token_url = 'https://api.line.me/oauth2/v2.1/token'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thesecretkey'
# login
def get_redirect_url():
    return url_for(
        '.oauth_callback',
        _external=True,
        _scheme='https'
    )
@app.route("/login")
def login():
    line_login = OAuth2Session(
        client_id, 
        redirect_uri=get_redirect_url(),
        scope='profile openid'
    )
    authorization_url, state = line_login.authorization_url(authorization_base_url)

    # State is used to prevent CSRF, keep this for later.
    session['oauth_state'] = state
    return redirect(authorization_url)

@app.route("/oauth_callback")
def oauth_callback():
    line_login = OAuth2Session(client_id, state=session['oauth_state'], redirect_uri=get_redirect_url())
    token = line_login.fetch_token(
        token_url, 
        client_secret=client_secret,
        authorization_response=request.url.replace('http', 'https')
    )

    return jsonify(line_login.get('https://api.line.me/v2/profile').json())

line_bot_api = LineBotApi('BzInYuQWZ2KDpjYaRX+nGGk092AQ7UgWHkRx7IT8J8Xc7mbP6gxzDLgcLCuuePJW7FknCq6k/d8RHjxsLoviwUndZB2uzTOJgb6K/PBk3hKjBzSa4te7peTFaFTBmFg2KSFUZmv8o4I3dh2Tm2et3wdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('a842e0251982aac19ce2ffd563f28d3c')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # 預設回覆與使用者相同訊息
    # line_bot_api.reply_message(
    #     event.reply_token,
    #     TextSendMessage(text=event.message.text))

    # 根據接收文字回傳特定訊息
    if event.message.text == '@info':
        line_bot_api.reply_message(
            event.reply_token,
            [
                TextSendMessage(text='hello'),
                StickerSendMessage(package_id='1', sticker_id='2')
            ]
        )
    else :
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='何言ってんの？分がんないよ〜')
        )


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
