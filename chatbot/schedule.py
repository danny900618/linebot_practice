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

# 「時刻表」按鈕樣板訊息
class Schedule():
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
                    "text": "Root_時刻表 選擇查看的組別",
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
                    "data": "Schedule：WEB",
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
                    "data": "Schedule：IOT",
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
                    "data": "Schedule：IOS",
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
                    "data": "Schedule：Android",
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
                    "data": "Schedule：碩班",
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
