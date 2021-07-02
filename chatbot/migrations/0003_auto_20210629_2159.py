# Generated by Django 3.2.4 on 2021-06-30 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0002_auto_20210628_2256'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_info',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='更新時間'),
        ),
        migrations.AlterField(
            model_name='user_info',
            name='name',
            field=models.CharField(blank=True, max_length=4),
        ),
    ]
