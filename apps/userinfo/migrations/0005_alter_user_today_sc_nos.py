# Generated by Django 4.2.8 on 2023-12-22 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0004_alter_user_today_sc_nos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='today_sc_nos',
            field=models.JSONField(blank=True, help_text='今日答题no', null=True),
        ),
    ]
