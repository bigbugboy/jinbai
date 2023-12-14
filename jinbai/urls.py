from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('user/', include('apps.userinfo.urls')),
    path('exercise/', include('apps.exercise.urls')),
]
