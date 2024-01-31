from django.urls import path
from main.apps import MainConfig
from main.views import CardListView

app_name = 'main'

urlpatterns = [
    path('', CardListView.as_view(), name='index'),
]