# Generated by Django 3.2.4 on 2021-07-01 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0022_user_info_day1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_info',
            old_name='day1',
            new_name='date_day1',
        ),
    ]