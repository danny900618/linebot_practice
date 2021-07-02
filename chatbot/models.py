from logging import root
from django.db import models
# Create your models here.
class User_Info(models.Model):
    uid = models.CharField(max_length=50,null=False,default='')         #user_id
    name = models.CharField(max_length=4,blank=True,null=False)       #LINE名字
    team = models.CharField(max_length=50,blank=True,null=False)      #組別
    date= models.CharField(max_length=50,blank=True,null=False)       #簽到時間
    yes_project= models.CharField(max_length=500,blank=True,null=False)    #昨日完成進度 
    tod_project= models.CharField(max_length=500,blank=True,null=False)    #今日規劃進度
    update_project=models.CharField(max_length=500,blank=True,null=False)    #專案更新時間
    root=models.CharField(max_length=1,default=0)   #判斷是否為管理員
    yesterday_temp=models.CharField(max_length=500,default=0)   #昨日暫存
    today_temp=models.CharField(max_length=500,default=0)       #今日暫存
    date_day1=models.CharField(max_length=50,blank=True,null=False)  #七天簽到時間歷史紀錄 day1
    date_day2=models.CharField(max_length=50,blank=True,null=False)  #七天簽到時間歷史紀錄 day2
    date_day3=models.CharField(max_length=50,blank=True,null=False)  #七天簽到時間歷史紀錄 day3
    date_day4=models.CharField(max_length=50,blank=True,null=False)  #七天簽到時間歷史紀錄 day4
    date_day5=models.CharField(max_length=50,blank=True,null=False)  #七天簽到時間歷史紀錄 day5
    date_day6=models.CharField(max_length=50,blank=True,null=False)  #七天簽到時間歷史紀錄 day6
    date_day7=models.CharField(max_length=50,blank=True,null=False)  #七天簽到時間歷史紀錄 day7
    def __str__(self):
        data = dict()
        data={
            'uid':self.uid,
            'name':self.name,
            'team':self.team,
            'date':self.date,
            'yes_project':self.yes_project,
            'tod_project':self.tod_project, 
            'update_project':self.update_project,  
            'root':self.root,
            'yesterday_temp':self.yesterday_temp,
            'today_temp':self.today_temp,
            'date_day1':self.date_day1,
            'date_day2':self.date_day2,
            'date_day3':self.date_day3,
            'date_day4':self.date_day4,
            'date_day5':self.date_day5,
            'date_day6':self.date_day6,
            'date_day7':self.date_day7
        }
        return str(data)