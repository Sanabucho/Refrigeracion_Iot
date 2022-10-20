from django.urls import path

from .views import *


urlpatterns = [
    path('data/list/', ListDataTSView.as_view()),
    path('data/register/', CreateDataTSView.as_view()),

]