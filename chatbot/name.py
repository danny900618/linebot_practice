from chatbot import report
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
class Name():
    def __init__(self):
        pass
    def content(self,str):
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
                    "text": "Root_時刻表 選擇姓名",
                    "size": "lg",
                    "color": "#ffffff"
                }
                ],
                "backgroundColor": "#0066ff"
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents":str                  
            }
            }
        )
        return flex_message

    