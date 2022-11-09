from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, StickerSendMessage, FollowEvent, UnfollowEvent,
    TemplateSendMessage, CarouselTemplate, CarouselColumn, URIAction
)

line_bot_api = LineBotApi('BzInYuQWZ2KDpjYaRX+nGGk092AQ7UgWHkRx7IT8J8Xc7mbP6gxzDLgcLCuuePJW7FknCq6k/d8RHjxsLoviwUndZB2uzTOJgb6K/PBk3hKjBzSa4te7peTFaFTBmFg2KSFUZmv8o4I3dh2Tm2et3wdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('a842e0251982aac19ce2ffd563f28d3c')
