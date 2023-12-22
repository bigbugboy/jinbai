import json

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):


    telephone = models.BigIntegerField(unique=True, blank=False, null=False)
    vip = models.BooleanField(default=False)
    today_sc_nos = models.JSONField(blank=True, null=True, help_text='今日答题no')
    collected_sc_nos = models.TextField(blank=True, null=True, help_text='用户收藏的单选题目no')
