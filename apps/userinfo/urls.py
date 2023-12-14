from django.urls import path

from . import views


urlpatterns = [
    path('login', views.LoginView.as_view(), name='login'),
    path('logut', views.logut, name='logut'),
    path('send-verify-code', views.SendVerifyCode.as_view(), name='send-verify-code'),
    path('validate-phone', views.ValidatePhone.as_view(), name='validate-phone'),

    path('console', views.console, name='console'),
]
