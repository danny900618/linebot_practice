from linebot.models.responses import Content
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

# 「功能列表」按鈕樣板訊息
class Featuresmodel():
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
                    "text": "功能列表",
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
                    "label": "註冊",
                    "data": "註冊",
                    },
                    "margin": "sm",
                    "color": "#0066ff",
                    "style": "primary"
                },
                {
                    "type": "button",
                    "action": {
                    "type": "postback",
                    "label": "簽到",
                    "data": "簽到",
                    },
                    "color": "#0066ff",
                    "style": "primary",
                    "margin": "sm"
                },
                {
                    "type": "button",
                    "action": {
                    "type": "postback",
                    "label": "專案進度",
                    "data": "專案進度",
                    },
                    "color": "#0066ff",
                    "margin": "sm",
                    "style": "primary"
                },
                {
                    "type": "button",
                    "action": {
                    "type": "postback",
                    "label": "本日尚未簽到",
                    "data": "本日尚未簽到"
                    },
                    "color": "#0066ff",
                    "style": "primary",
                    "margin": "sm"
                },
                {
                    "type": "button",
                    "action": {
                    "type": "postback",
                    "label": "時刻表",
                    "data": "時刻表"
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
        
