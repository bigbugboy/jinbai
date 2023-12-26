import json
import random
from datetime import date

from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.http import HttpRequest, HttpResponseBadRequest, Http404
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from . import models


@method_decorator(login_required(login_url='login'), name='get')
@method_decorator(login_required(login_url='login'), name='post')
class SingleChoice(View):

    def get(self, request: HttpRequest):
        vip = request.user.vip
        star = request.GET.get('star', 1) if vip else 1
        if not star.isdigit() or int(star) not in [s[0] for s in models.SingleChoice.star_choices]:
            raise Http404()
        
        # 过滤出来满足条件的上架题目
        scs = models.SingleChoice.objects.filter(star=int(star), status=2).all()
        if not scs:
            raise Http404()
        
        sc = random.choice(scs)
        context = {
            'sc': sc,
            'star': str(star),
        }
        request.session['todo_sc_no'] = sc.no
        return render(request, 'exercise.html', context) 

    def post(self, request: HttpRequest):
        sc_no = request.headers['sc-no']
        select_choice = request.headers['choice']

        if request.session.get('todo_sc_no') != sc_no:
            return HttpResponseBadRequest('bad')
        
        sc = get_object_or_404(models.SingleChoice, no=sc_no)
        answer_correct = sc.right_choice == select_choice
        sc.update_stats(answer_correct)
        request.user.update_today_sc_nos(sc_no, answer_correct)
        del request.session['todo_sc_no']
        return HttpResponse('ok')



@method_decorator(login_required(login_url='login'), name='get')
class SingleChoiceDailyDetail(View):

    def get(self, request: HttpRequest, no):
        if no not in request.user.get_today_sc_nos():
            return redirect(to='single-choice')
        
        sc = get_object_or_404(models.SingleChoice, no=no)
        context = {'sc': sc}
        request.session['todo_sc_no'] = sc.no
        return render(request, 'exercise.html', context)
