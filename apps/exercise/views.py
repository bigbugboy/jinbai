import json
import random
from datetime import date

from django.contrib import messages
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.http import HttpRequest, JsonResponse, Http404
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

        scs = models.SingleChoice.objects.filter(star=star, status=2).all()
        sc = random.choice(scs)
        context = {
            'sc': sc,
        }
        return render(request, 'exercise.html', context)

    def post(self, request: HttpRequest):
        sc_no = request.headers['sc-no']
        select_choice = request.headers['choice']
       
        sc = get_object_or_404(models.SingleChoice, no=sc_no)
        sc.update_stats(sc.right_choice == select_choice)
        return HttpResponse('ok')

