# Generated by Django 4.2.8 on 2023-12-15 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='sc_ids',
        ),
        migrations.AddField(
            model_name='user',
            name='sc_nos',
            field=models.TextField(blank=True, help_text='用户管收藏的单选题目no', null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='today_sc_nos',
            field=models.CharField(default='', help_text='今日答题no', max_length=1000),
        ),
    ]
