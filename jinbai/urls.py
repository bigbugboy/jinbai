import os
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.conf import settings
from django.http.response import FileResponse


def index(request):
    return render(request, 'index.html')


def favicon(request):
    filepath = os.path.join(settings.BASE_DIR, 'static', 'img', 'favicon.ico')
    return FileResponse(open(filepath, 'rb'), filename='favicon.ico')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('favicon.ico', favicon, name='favicon'),
    path('user/', include('apps.userinfo.urls')),
    path('console/', include('apps.console.urls')),
    path('exercise/', include('apps.exercise.urls')),
]
