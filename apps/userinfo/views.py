from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpRequest

from  . import models


class LoginView(View):
    def get(self, request):
        next_page = request.GET.get('next')
        if next_page:
            print(next_page)
            messages.info(request, '请先登录哦！')
        return render(request, 'login.html')

    def post(self, request):
        telephone = request.POST.get('telephone')
        verify_code = request.POST.get('code')
        if not telephone or not verify_code:
            messages.error(request, '手机号或验证码不能为空')
            return render(request, 'login.html')
        # todo: validate verify code and telephone
        # todo: send verify code by cloud api
        user, is_created  = models.User.objects.get_or_create(
            telephone=telephone, 
            defaults={'telephone': telephone, 'username': str(telephone)}
        )
        auth.login(request, user)
        messages.success(request, f'欢迎:{user.telephone}')
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