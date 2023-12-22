from django.db import models
from ckeditor.fields import RichTextField


class Tag(models.Model):
    objects: models.QuerySet
    name = models.CharField(max_length=32, unique=True, blank=False, null=False)
    description = models.CharField(max_length=255, default='', blank=True)

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name


    def __str__(self) -> str:
        return self.name



class SingleChoice(models.Model):
    objects: models.query.QuerySet

    status_choices = (
        (1, '待上架'),
        (2, '上架'),
        (0, '下架'),
    )

    tag = models.ForeignKey(to=Tag, on_delete=models.SET_NULL, null=True)
    star = models.SmallIntegerField(default=1, choices=((i + 1, f'{i+1}颗星')for i in range(3)), help_text='难度系数')
    no = models.CharField(max_length=10, blank=False, null=False, unique=True, help_text='题目唯一编号')
    title = RichTextField(blank=False, null=False)
    choice_a = RichTextField(max_length=255, null=False)
    choice_b = RichTextField(max_length=255, null=False)
    choice_c = RichTextField(max_length=255, null=False)
    choice_d = RichTextField(max_length=255, null=False)
    right_choice = models.CharField(max_length=1, choices=((c, str(c).upper()) for c in 'abcd'), blank=False, null=False)
    description = RichTextField(default='')
    status = models.SmallIntegerField(default=1, choices=status_choices, help_text='题目的状态')
    created_at = models.DateTimeField(auto_now_add=True, help_text='创建时间')
    updated_at = models.DateTimeField(auto_now=True, help_text='更新时间')
    # 统计信息
    right_counts = models.IntegerField(default=0, help_text='答对次数')
    wrong_counts = models.IntegerField(default=0, help_text='答错次数')
    collect_counts = models.IntegerField(default=0, help_text='被用户收藏次数')

    class Meta:
        verbose_name = '单选题'
        verbose_name_plural = verbose_name
    
    def update_stats(self, answer_correct: bool):
        if answer_correct:
            self.right_counts += 1
        else:
            self.wrong_counts += 1
        try:
            self.save()
        except Exception as e:
            pass