from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    vip_choices = (
        (0, ''),
        (7, '7天'),
        (14, '14天'),
        (30, '30天'),
    )

    telephone = models.BigIntegerField(unique=True, blank=False, null=False)
    vip = models.BooleanField(default=False)
    vip_type = models.SmallIntegerField(choices=vip_choices, default=0)
    vip_start_date = models.DateTimeField(blank=True, null=True)
    vip_end_date = models.DateTimeField(blank=True, null=True)

    sc_ids = models.TextField(blank=True, null=True, help_text='用户管收藏的单选题目ID')
    

