# Generated by Django 4.2.8 on 2023-12-22 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0005_alter_user_today_sc_nos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='sc_nos',
        ),
        migrations.RemoveField(
            model_name='user',
            name='vip_end_date',
        ),
        migrations.RemoveField(
            model_name='user',
            name='vip_start_date',
        ),
        migrations.RemoveField(
            model_name='user',
            name='vip_type',
        ),
        migrations.AddField(
            model_name='user',
            name='collected_sc_nos',
            field=models.TextField(blank=True, help_text='用户收藏的单选题目no', null=True),
        ),
    ]
