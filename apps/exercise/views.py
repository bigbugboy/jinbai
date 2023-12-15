import random
from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, JsonResponse, HttpResponseForbidden
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from . import models


def index(request):
    return render(request, 'exercise.html')



@method_decorator(login_required, name='get')
@method_decorator(login_required, name='post')
class ScStart(View):

    def _json_to(self, sc: models.SingleChoice):
        return {
            'no': sc.no,
            'tags': [tag for tag in sc.tags.all().values()], 
            'star': sc.star,
            'title': sc.title,
            'choice_a': sc.choice_a,
            'choice_b': sc.choice_b,
            'choice_c': sc.choice_c,
            'choice_d': sc.choice_d,
            'right_counts': sc.right_choice,
            'wrong_counts': sc.wrong_counts,
            'collect_counts': sc.collect_counts,
        }

    def get(self, request: HttpRequest):
        vip = request.user.vip
        star = request.headers.get('star', 1)
        todo_sc_no = request.session.get('todo_sc_no')
        if todo_sc_no:
            sc = get_object_or_404(models.SingleChoice, no=todo_sc_no)
            print(111)
            print()
            return JsonResponse(self._json_to(sc))
        
        # 新的题目
        scs = models.SingleChoice.objects.filter(star=1, status=2).all()
        if vip:
          scs = models.SingleChoice.objects.filter(star=star, status=2).all()

        sc = random.choice(scs)
        request.session['todo_sc_no'] = sc.no
        return JsonResponse(self._json_to(sc))


    def post(self, request: HttpRequest):
        todo_sc_no = request.headers['todo-sc-no']
        right_choice = request.headers['right-choice']
        sc = get_object_or_404(models.SingleChoice, no=todo_sc_no)
        print(sc.right_choice)
        print(right_choice)
        return JsonResponse({
            'status': right_choice == sc.right_choice,
            'rc': sc.right_choice,
            'desc': sc.description,
        })

