from django.contrib import admin

# Register your models here.
from chatbot.models import *

class User_Info_Admin(admin.ModelAdmin):
    list_display = ('uid','name','team')
admin.site.register(User_Info,User_Info_Admin)
