# Generated by Django 3.2.4 on 2021-06-30 03:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0011_alter_user_info_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_info',
            name='date',
        ),
    ]
