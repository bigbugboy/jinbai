from datetime import date

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http.request import HttpRequest

from apps.exercise.models import SingleChoice


@login_required(login_url='login')
def icenter(request: HttpRequest):
    today = date.today()
    today_sc_nos = request.user.today_sc_nos.get(str(today), [])
    context = {
        'today_sc_counts': len(today_sc_nos),
        'collected_sc_counts': 0,
    }
    return render(request, 'console/icenter.html', context)


@login_required(login_url='login')
def dailysc(request):
    request.user.today_sc_nos
    data = SingleChoice.objects.filter(no__in=[item.no for item in request.user.today_sc_nos]).all()
    # todo: 需要展示哪些数据，如何展示？
    context = {
        'daily_stats':[]
    }
    return render(request, 'console/dailysc.html', context)


@login_required(login_url='login')
def lovesc(request):
    return render(request, 'console/lovesc.html')


@login_required(login_url='login')
def editphone(request):
    return render(request, 'console/editphone.html')


@login_required(login_url='login')
def bindemail(request):
    return render(request, 'console/bindemail.html')
