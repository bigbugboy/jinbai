from django.urls import path

from . import views


urlpatterns = [
    path('single-choice', views.SingleChoice.as_view(), name='single-choice'),
    path('sc-daily-detail/<no>', views.SingleChoiceDailyDetail.as_view(), name='sc-daily-detail'),
]