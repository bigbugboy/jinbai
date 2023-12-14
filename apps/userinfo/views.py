from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpRequest

from  . import models


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        telephone = request.POST.get('telephone')
        verify_code = request.POST.get('code')
        
        user = models.User.objects.create_user(username=str(telephone), telephone=telephone)
        auth.login(request, user)
        return redirect(to='index')


def logut(request):
    auth.logout(request)
    return redirect('index')


class SendVerifyCode(View):
    def post(self, request):
        telephone = request.POST.get('telephone')
        return JsonResponse({'code': 0, 'msg': 'OK'})


class ValidatePhone(View):
    def post(self, request):
        telephone = request.POST.get('telephone')
        return JsonResponse({'code': 0, 'msg': 'OK'})
    


@login_required(login_url='login')
def console(request: HttpRequest):
    request.x_hash = request.GET.get('hash')
    return render(request, 'consoles/index.html')

