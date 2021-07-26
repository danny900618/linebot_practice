import json,ast
from django.db.models.query import QuerySet
from django.http.response import JsonResponse
from chatbot import urls
from django.db.models.fields import EmailField
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
 
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
from .message import Featuresmodel, Message
from .team import Team
from .report import Report
from .schedule import Schedule
from .root_team import Root_Team
from .name import Name
from chatbot.models import *
from datetime import datetime, timezone, timedelta
from chatbot import schedule
line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)
# Create your views here.

@csrf_exempt
def callback(request):
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
            if isinstance(event, MessageEvent):  # 如果有normal訊息事件                
                if event.message.text == "功能列表":
                    line_bot_api.reply_message(  # 回復「功能列表」按鈕樣板訊息
                        event.reply_token,
                        Featuresmodel().content()   
                    )
                if event.message.text[0] == "姓":
                    uid=event.source.user_id
                    name=event.message.text[3:]
                    if is_all_chinese(name)==True:
                        message=[]
                        if User_Info.objects.filter(name=name).exists()==True:
                            line_bot_api.reply_message( 
                            event.reply_token,
                            TextSendMessage(text="已經有建立會員資料囉") 
                            )
                        # elif User_Info.objects.filter(uid=uid).exists()==True:
                        #     line_bot_api.reply_message( 
                        #     event.reply_token,
                        #     TextSendMessage(text="已經有建立會員資料囉") 
                        #     )
                        else:
                            User_Info.objects.create(uid=uid,name=name)
                            line_bot_api.reply_message( 
                            event.reply_token,
                            Team().content()
                            )
                    else :
                        line_bot_api.reply_message(  
                            event.reply_token,
                            TextSendMessage(text="請輸入中文名字") 
                            )
                if event.message.text[:9] == "[昨日完成進度]：":
                    uid=event.source.user_id
                    user=User_Info.objects.get(uid=uid)
                    user.yesterday_temp=event.message.text[9:]#將使用者輸入的昨日完成進度暫存到資料庫
                    user.save()
                    line_bot_api.reply_message(  # 回復「功能列表」按鈕樣板訊息
                        event.reply_token,
                        TextSendMessage(text="請輸入\n"+"[今日規劃進度]：") 
                    )
                if event.message.text[:9] == "[今日規劃進度]：":
                    uid=event.source.user_id
                    user=User_Info.objects.get(uid=uid)
                    user.today_temp=event.message.text[9:] #將使用者輸入的今日規劃進度暫存到資料庫
                    user.save()
                    line_bot_api.reply_message(  # 回復「功能列表」按鈕樣板訊息
                        event.reply_token,
                        TextSendMessage(text="確認是否要修改成\n"+"[昨日完成進度]："+user.yesterday_temp+"\n"+"[今日規劃進度]："+user.today_temp+"\n"+"Y/N")
                    )
                if event.message.text== "Y":
                    tz = timezone(timedelta(hours=+8))
                    now=datetime.now(tz).isoformat()
                    today = str(now)[:19]
                    uid=event.source.user_id 
                    user=User_Info.objects.get(uid=uid)
                    user.yes_project=user.yesterday_temp
                    user.tod_project=user.today_temp
                    user.update_project=today
                    user.save()
                    user.yesterday_temp=0
                    user.today_temp=0
                    user.save()
                    line_bot_api.reply_message( 
                        event.reply_token,
                        TextSendMessage(text="專案進度修改成功\n"+"當前的專案進度：\n"+"[昨日完成進度]："+user.yes_project+"\n"+"[今日規劃進度]："+user.tod_project)
                    )
                if event.message.text== "N":
                    uid=event.source.user_id
                    user=User_Info.objects.get(uid=uid)
                    user.yesterday_temp=0
                    user.today_temp=0
                    user.save()
                    line_bot_api.reply_message( 
                        event.reply_token,
                        TextSendMessage(text="你已放棄專案修改\n"+"當前的專案進度：\n"+"[昨日完成進度]："+user.yes_project+"\n"+"[今日規劃進度]："+user.tod_project)
                    )
                if event.message.text[:9] == "[我要成為管理員]":
                    uid=event.source.user_id
                    user=User_Info.objects.get(uid=uid)
                    user.root=1 #將使用者晉升為管理員
                    user.save()
                    line_bot_api.reply_message(  
                        event.reply_token,
                        TextSendMessage(text="你已經成為管理員")
                    )

            if isinstance(event, PostbackEvent):  # 如果有normal訊息事件
                #以下為按鈕“註冊按鈕“

                if event.postback.data[0] == "註" and event.postback.data[1] == '冊':
                    line_bot_api.reply_message(
                        event.reply_token,
                        TextSendMessage(text="請輸入姓名：\n"+"格式如下\n"+"姓名：") 
                    )
                if event.postback.data[0] == "組" and event.postback.data[1] == '別':
                    team=str(event.postback.data[3:])
                    if User_Info.objects.filter(team=team).exists()==True:
                        line_bot_api.reply_message(  # 回復「功能列表」按鈕樣板訊息
                        event.reply_token,
                        TextSendMessage(text="已經有建立會員資料囉") 
                        )
                    else:
                        uid=event.source.user_id
                        user=User_Info.objects.get(uid=uid)
                        user.yesterday=1
                        user.save()
                        line_bot_api.reply_message(  
                        event.reply_token,
                        TextSendMessage(text="註冊完畢") 
                        )
                    #以下為按鈕“簽到“
                if event.postback.data[0] == "簽" and event.postback.data[1] == '到':
                    tz = timezone(timedelta(hours=+8))
                    now=datetime.now(tz).isoformat()
                    # now = (datetime.datetime.now()).isoformat()   #獲取當下時間
                    today = str(now)[:19]
                    uid=event.source.user_id
                    user=User_Info.objects.get(uid=uid)
                    user.date=today
                    user.date_day1=today
                    user.save()
                    line_bot_api.reply_message(
                        event.reply_token,
                        TextSendMessage(text="簽到完畢\n"+"簽到時間為："+today) 
                    )
                    #以下為按鈕“專案進度“
                if event.postback.data[0] == "專" and event.postback.data[1] == '案':
                    line_bot_api.reply_message(
                        event.reply_token,
                        Report().content()  #回復「專案進度」按鈕樣板訊息
                        # TextSendMessage(text=Report().content()) 
                    )
                if event.postback.data[0] == "回" and event.postback.data[1] == '報':
                    uid=event.source.user_id
                    user=User_Info.objects.get(uid=uid)
                    line_bot_api.reply_message(
                        event.reply_token,
                        TextSendMessage(text="[昨日完成進度]："+user.yes_project+"\n\n"+"[今日規劃進度]："+user.tod_project) 
                    )
                if event.postback.data[0] == "修" and event.postback.data[1] == '改':
                    uid=event.source.user_id
                    user=User_Info.objects.get(uid=uid)
                    line_bot_api.reply_message(
                        event.reply_token,
                        TextSendMessage(text="請輸入\n"+"[昨日完成進度]：") 
                    )
                if event.postback.data[0] == "查" and event.postback.data[1] == '看':  #不是管理員身份
                    uid=event.source.user_id
                    user=User_Info.objects.get(uid=uid)
                    if user.root =="1":
                        line_bot_api.reply_message(
                            event.reply_token,
                            Root_Team().content()
                        )
                    else :
                        line_bot_api.reply_message(
                            event.reply_token,
                            TextSendMessage(text="你不是管理員無法使用") 
                        )
                #獲得管理權限後查看＿選則組別
                if event.postback.data[:5] == "Root：":
                    choose=str(event.postback.data[5:]) #選擇要的組別名稱
                    # user=User_Info.objects.filter(team=choose)
                    all=''
                    for data in User_Info.objects.filter(team=choose):
                        if data.update_project == "":
                            data.update_project="[本日尚未回報進度]"
                        message="姓名："+data.name+"\n"+"組別："+data.team+"\n"+"[昨日完成進度]："+data.yes_project+"\n"+"[今日規劃進度]："+data.tod_project+"\n"+"[專案進度更新時間]："+data.update_project+"\n\n"
                        all=all+message
                    line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=all) 
                    )
                #本日尚未簽到的按鈕
                if event.postback.data[0] == "本" and event.postback.data[1] == '日':
                    all=""
                    for data in User_Info.objects.filter(date=""):
                        message="姓名："+data.name+"\n"+"組別："+data.team+"\n\n"
                        all=all+message
                    line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text="[本日尚未簽到的使用者]\n"+all) 
                    )
                #時刻表的按鈕
                if event.postback.data[0] == "時" and event.postback.data[1] == '刻':
                    uid=event.source.user_id
                    user=User_Info.objects.get(uid=uid)
                    if user.root =="1":
                        line_bot_api.reply_message(
                        event.reply_token,
                        Schedule().content() #回復「時刻表」按鈕樣板訊息
                        )
                    else :
                        line_bot_api.reply_message(
                            event.reply_token,
                            TextSendMessage(text="你不是管理員無法使用") 
                        )
                #時刻表選取的組別
                if event.postback.data[:9] == "Schedule：":
                    choose=str(event.postback.data[9:]) #選擇 時刻表 要的查看組別名稱
                    list=[]
                    for data in User_Info.objects.filter(team=choose):
                        new_body={
                                "type": "button",
                                "action": {
                                "type": "postback",
                                "label": data.name,
                                "data": "Name="+data.name
                                },
                                "margin": "sm",
                                "color": "#0066ff",
                                "style": "primary"
                            }
                        list.append(dict(new_body))                
                    line_bot_api.reply_message(
                        event.reply_token,
                        Name().content(list)
                    )
                if event.postback.data[:5] == "Name=":#選擇時刻表_姓名後列出項目
                    data=User_Info.objects.get(name=event.postback.data[5:])
                    if data.update_project == "":
                        data.update_project="[本日尚未回報進度]"
                    line_bot_api.reply_message(
                        event.reply_token,
                        TextSendMessage(text="姓名："+data.name+"\n"+"[最新簽到時間]："+data.date+"\n"+"[近期七天簽到時間]："+data.date_day1+"\n")
                    )
        return HttpResponse()
    else:
        return HttpResponseBadRequest()


#檢驗是否全是中文字符
def is_all_chinese(strs):
    for _char in strs:
        if not '\u4e00' <= _char <= '\u9fa5':
            return False
    return True
