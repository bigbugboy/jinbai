from django.urls import path

from . import views


urlpatterns = [
    path('icenter', views.icenter, name='icenter'),
]
