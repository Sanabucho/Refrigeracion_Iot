from re import template
from django.urls import path
from django.conf.urls import url
from django.views.generic.base import TemplateView
from .views import *


urlpatterns = [
    path('data/list/', ListDataTSView.as_view()),
    path('data/register/', CreateDataTSView.as_view()),
    path('', index, name='index'),

]