# Generated by Django 4.2.8 on 2023-12-13 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='sc_ids',
            field=models.TextField(blank=True, help_text='用户收藏的单选题目ID', null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='vip',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='vip_end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='vip_start_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='vip_type',
            field=models.SmallIntegerField(choices=[(0, ''), (7, '7天'), (14, '14天'), (30, '30天')], default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='telephone',
            field=models.BigIntegerField(unique=True),
        ),
    ]
