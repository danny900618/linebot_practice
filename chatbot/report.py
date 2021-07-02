import requests
from abc import ABC, abstractmethod
from linebot.models import TemplateSendMessage , ButtonsTemplate, PostbackAction , MessageAction , URIAction , CarouselColumn , CarouselTemplate , PostbackTemplateAction , FlexSendMessage
# from pymongo import MongoClient
from bs4 import BeautifulSoup

# 訊息抽象類別
class Message(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def content(self):
        pass

# 「專案進度」按鈕樣板訊息
class Report():
    def content(self):
        flex_message = FlexSendMessage(
            alt_text='hello',
            contents={
            "type": "bubble",
            "header": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "專案進度",
                    "size": "lg",
                    "color": "#ffffff"
                }
                ],
                "backgroundColor": "#0066ff"
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "button",
                    "action": {
                    "type": "postback",
                    "label": "回報",
                    "data": "回報",
                    "displayText": "回報"
                    },
                    "margin": "sm",
                    "color": "#0066ff",
                    "style": "primary"
                },
                {
                    "type": "button",
                    "action": {
                    "type": "postback",
                    "label": "修改",
                    "data": "修改",
                    "displayText": "修改"
                    },
                    "color": "#0066ff",
                    "style": "primary",
                    "margin": "sm"
                },
                {
                    "type": "button",
                    "action": {
                    "type": "postback",
                    "label": "查看",
                    "data": "查看",
                    "displayText": "查看"
                    },
                    "color": "#0066ff",
                    "margin": "sm",
                    "style": "primary"
                }
                ]
            }
            }
        )
        return flex_message
