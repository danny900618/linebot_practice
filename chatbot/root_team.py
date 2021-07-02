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

# 「管理員查看」按鈕樣板訊息
class Root_Team():
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
                    "text": "Root_選擇查看的組別",
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
                    "label": "WEB",
                    "data": "Root：WEB",
                    "displayText": "組別：WEB"
                    },
                    "margin": "sm",
                    "color": "#0066ff",
                    "style": "primary"
                },
                {
                    "type": "button",
                    "action": {
                    "type": "postback",
                    "label": "IOT",
                    "data": "Root：IOT",
                    "displayText": "組別：IOT"
                    },
                    "color": "#0066ff",
                    "style": "primary",
                    "margin": "sm"
                },
                {
                    "type": "button",
                    "action": {
                    "type": "postback",
                    "label": "IOS",
                    "data": "Root：IOS",
                    "displayText": "組別：IOS"
                    },
                    "color": "#0066ff",
                    "margin": "sm",
                    "style": "primary"
                },
                {
                    "type": "button",
                    "action": {
                    "type": "postback",
                    "label": "Android",
                    "data": "Root：Android",
                    "displayText": "組別：Android"
                    },
                    "color": "#0066ff",
                    "style": "primary",
                    "margin": "sm"
                },
                {
                    "type": "button",
                    "action": {
                    "type": "postback",
                    "label": "碩班",
                    "data": "Root：碩班",
                    "displayText": "組別：碩班"
                    },
                    "color": "#0066ff",
                    "style": "primary",
                    "margin": "sm"
                }
                ]
            }
            }
        )
        return flex_message
