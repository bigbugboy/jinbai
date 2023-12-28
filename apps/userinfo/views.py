from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from django.core.cache import cache
from django.conf import settings
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpRequest
from django.views.decorators.http import require_POST
from  . import models, forms, utils


def logut(request):
    auth.logout(request)
    return redirect('index')


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
        form_obj = forms.LoginForm({'telephone': telephone, 'verify_code': verify_code})
        if form_obj.is_valid():
            user, is_created  = models.User.objects.get_or_create(
                telephone=telephone, 
                defaults={'telephone': telephone, 'username': str(telephone)}
            )
            auth.login(request, user)
            cache.delete(settings.TELEPHONE_VERIFY_CODE_KEY % telephone)
            messages.success(request, f'欢迎:{user.telephone}')
            return redirect(to='index')
        
        # validate failed
        messages.error(request, '手机号或验证码错误')
        return render(request, 'login.html')


@require_POST
def send_verify_code(request: HttpRequest):
    telephone = request.headers.get('telephone')
    if not utils.validate_telephone(telephone):
        return JsonResponse({'status': 'error', 'msg': '手机号错误'})
    
    key = settings.TELEPHONE_VERIFY_CODE_KEY % telephone
    if cache.get(key):
        return JsonResponse({'status': 'error', 'msg': '1分钟以后再发送验证码'})
    
    code = utils.generate_verify_code()
    cache.set(key, code, timeout=settings.TELEPHONE_VERIFY_CODE_TIMEOUT)
    # todo send code call cloud api
    print('verify code:', code)
    return JsonResponse({'status': 'success', 'msg': 'ok'})
