# Generated by Django 3.2.4 on 2021-06-30 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0016_auto_20210630_0148'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_info',
            name='root',
            field=models.CharField(default=0, max_length=1),
        ),
    ]
