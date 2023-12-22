import json
from datetime import date

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):


    telephone = models.BigIntegerField(unique=True, blank=False, null=False)
    vip = models.BooleanField(default=False)
    today_sc_nos = models.JSONField(default=dict, help_text='今日答题no')
    collected_sc_nos = models.TextField(blank=True, null=True, help_text='用户收藏的单选题目no')

    def update_today_sc_nos(self, no, answer_correct):
        today = str(date.today())
        nos = self.today_sc_nos.get(today, [])
        if no not in nos:
            nos.append({'no': no, 'ac': answer_correct})
        self.today_sc_nos = {today: sorted(nos, key=lambda x: x['no'])}
        self.save()