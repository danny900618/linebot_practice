# Generated by Django 3.2.4 on 2021-07-02 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0023_rename_day1_user_info_date_day1'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_info',
            name='date_day2',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='user_info',
            name='date_day3',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='user_info',
            name='date_day4',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='user_info',
            name='date_day5',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='user_info',
            name='date_day6',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='user_info',
            name='date_day7',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]