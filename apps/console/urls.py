from django.urls import path

from . import views


urlpatterns = [
    path('icenter', views.icenter, name='icenter'),
    path('dailysc', views.dailysc, name='dailysc'),
    path('lovesc', views.lovesc, name='lovesc'),
    path('bindemail', views.bindemail, name='bindemail'),
    path('bindphone', views.BindPhoneView.as_view(), name='bindphone'),
]
