# urls.py
from django.urls import path
from .views import news_list, scrape, save_news

urlpatterns = [
    path('dashboard/', news_list, name='dashboard'),
    path('scrape/', scrape, name='scrape'),
]
