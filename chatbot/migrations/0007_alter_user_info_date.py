# Generated by Django 3.2.4 on 2021-06-30 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0006_auto_20210629_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_info',
            name='date',
            field=models.DateTimeField(default=''),
        ),
    ]