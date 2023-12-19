from django.urls import path

from . import views


urlpatterns = [
    path('login', views.LoginView.as_view(), name='login'),
    path('logut', views.logut, name='logut'),
    path('send-verify-code', views.send_verify_code, name='send-verify-code'),
]
