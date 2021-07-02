from django.db.models.query import QuerySet
from django.http.response import JsonResponse
from chatbot import urls
from django.db.models.fields import EmailField
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from chatbot.models import *
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import (
    MessageEvent,
    TextSendMessage,
	PostbackEvent
)
from linebot.models.events import Postback
from linebot.models.responses import Content, Profile
from linebot.models.sources import Source
line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)
def my_scheduled_job():
    user=User_Info.objects.all()
    User_Info.objects.all().update(date_day7=user.date_day6)
    User_Info.objects.all().update(date_day6=user.date_day5)
    User_Info.objects.all().update(date_day5=user.date_day4)
    User_Info.objects.all().update(date_day4=user.date_day3)
    User_Info.objects.all().update(date_day3=user.date_day2)
    User_Info.objects.all().update(date_day2=user.date_day1)
    User_Info.objects.all().update(date_day1=user.tod_project)
    User_Info.objects.all().update(tod_project="")

def my_scheduled_job2():
    if User_Info.objects.filter(root=1):
        
        if request.method == 'POST':
            signature = request.META['HTTP_X_LINE_SIGNATURE']
            body = request.body.decode('utf-8')
    
            try:
                events = parser.parse(body, signature)  # 傳入的事件
            except InvalidSignatureError:
                return HttpResponseForbidden()
            except LineBotApiError:
                return HttpResponseBadRequest()
    
            for event in events:
                if isinstance(event, MessageEvent):  # 如果有訊息事件
                    line_bot_api.reply_message(  # 回復傳入的訊息文字
                        event.reply_token,
                        TextSendMessage(text=event.message.text)
                    )
