from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http.request import HttpRequest
from django.views import View
from django.contrib import messages

from apps.exercise.models import SingleChoice
from apps.userinfo import forms, models as userinfo_models


@login_required(login_url='login')
def icenter(request: HttpRequest):
    today_sc_nos = request.user.get_today_sc_nos()
    context = {
        'today_sc_counts': len(today_sc_nos),
        'collected_sc_counts': 0,
    }
    return render(request, 'console/icenter.html', context)


@login_required(login_url='login')
def dailysc(request):
    today_sc_nos = request.user.get_today_sc_nos()
    data = SingleChoice.objects.filter(no__in=list(today_sc_nos.keys())).all()
    # todo: 需要展示哪些数据，如何展示？
    context = {
        'daily_sc_stats':[
            {
                'no': sc.no,
                'tag': sc.tag.name,
                'correct': today_sc_nos[sc.no]['ac'],
            }
            for sc in data
        ]
    }
    return render(request, 'console/dailysc.html', context)


@login_required(login_url='login')
def lovesc(request):
    context = {
        'loved_sc_stats':[]
    }
    return render(request, 'console/lovesc.html', context)


@method_decorator(login_required(login_url='login'), name='get')
@method_decorator(login_required(login_url='login'), name='post')
class BindPhoneView(View):
    def get(self, request):
        edit_page = request.GET.get('edit')
        return render(request, 'console/bindphone.html', context={'edit_page': edit_page})

    def post(self, request):
        telephone = request.POST.get('telephone')
        verify_code = request.POST.get('code')
        form_obj = forms.LoginForm({'telephone': telephone, 'verify_code': verify_code})
        if form_obj.is_valid():
            user = get_object_or_404(userinfo_models.User, telephone=request.user.telephone)
            user.telephone = telephone
            user.save()
            messages.success(request, f'手机号修改成功，新手机号：{telephone}')
            return redirect(to='bindphone')
        
        # validate failed
        messages.error(request, '手机号或验证码错误')
        return render(request, 'console/bindphone.html', context={'edit_page': True})


@login_required(login_url='login')
def bindemail(request):
    return render(request, 'console/bindemail.html')
