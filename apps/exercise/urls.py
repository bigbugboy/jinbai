from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='exercise'),
    path('scstart', views.ScStart.as_view(), name='scstart'),
]