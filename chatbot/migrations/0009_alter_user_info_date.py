# Generated by Django 3.2.4 on 2021-06-30 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0008_alter_user_info_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_info',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
