# Generated by Django 4.2.8 on 2023-12-22 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0007_alter_user_today_sc_nos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='today_sc_nos',
            field=models.JSONField(default=dict, help_text='今日答题no'),
        ),
    ]
