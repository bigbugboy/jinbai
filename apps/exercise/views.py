import json
import random
from datetime import date

from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, JsonResponse, Http404
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from . import models


@login_required(login_url='login')
def index(request):
    return render(request, 'exercise.html')


@method_decorator(login_required(login_url='login'), name='get')
@method_decorator(login_required(login_url='login'), name='post')
class ScStart(View):

    DAILY_SC_COUNTS = 74


    def _validate_user_nos(self, user):
        today = str(date.today())
        today_nos = json.loads(user.today_sc_nos)
        nos = today_nos.get(today, [])
        if len(nos) >= self.DAILY_SC_COUNTS:
            return False, nos
        return True, nos

    def _update_user_nos(self, user, no):
        today = str(date.today())
        today_nos = json.loads(user.today_sc_nos)
        nos = today_nos.get(today, [])
        nos.append(no)
        today_nos = {today: nos}
        user.today_sc_nos = json.dumps(today_nos)
        user.save()


    def _json_to(self, sc: models.SingleChoice, daily_sc_no_counts):
        return {
            'no': sc.no,
            'tag': sc.tag.name ,
            'star': sc.star,
            'title': sc.title,
            'choice_a': sc.choice_a,
            'choice_b': sc.choice_b,
            'choice_c': sc.choice_c,
            'choice_d': sc.choice_d,
            'right_counts': sc.right_counts,
            'wrong_counts': sc.wrong_counts,
            'collect_counts': sc.collect_counts,
            'daily_sc_counts': self.DAILY_SC_COUNTS,
            'left_sc_counts': max(self.DAILY_SC_COUNTS - daily_sc_no_counts, 0)
        }

    def get(self, request: HttpRequest):
        allow_next, daily_sc_nos = self._validate_user_nos(request.user)
        if not allow_next:
            # 今日答题次数已用完
            sc = get_object_or_404(models.SingleChoice, no=daily_sc_nos[-1])
            messages.info(request, '今日答题次数已用完')
            return JsonResponse(self._json_to(sc, len(daily_sc_nos)))
        
        vip = request.user.vip
        star = request.headers.get('star', 1)
        todo_sc_no = request.session.get('todo_sc_no')
        if todo_sc_no:
            sc = get_object_or_404(models.SingleChoice, no=todo_sc_no)
            return JsonResponse(self._json_to(sc, len(daily_sc_nos)))
        
        # 新的题目
        scs = models.SingleChoice.objects.filter(star=1, status=2).all()
        if vip:
          scs = models.SingleChoice.objects.filter(star=star, status=2).all()

        sc = random.choice(scs)
        request.session['todo_sc_no'] = sc.no
        return JsonResponse(self._json_to(sc, len(daily_sc_nos)))

    def post(self, request: HttpRequest):
        allow_next, _ = self._validate_user_nos(request.user)
        if not allow_next:
            raise Http404('upper limit reached')
        todo_sc_no = request.headers['todo-sc-no']
        select_choice = request.headers['select-choice']
        if todo_sc_no != request.session['todo_sc_no']:
            raise Http404()
        sc = get_object_or_404(models.SingleChoice, no=todo_sc_no)
        request.session['todo_sc_no'] = ''  # 这样操作后，下一题就会再随机一个新题
        self._update_user_nos(request.user, todo_sc_no)
        return JsonResponse({
            'status': select_choice == sc.right_choice,
            'right_choice': sc.right_choice,
            'desc': sc.description,
        })

