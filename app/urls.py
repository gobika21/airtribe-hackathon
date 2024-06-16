from .views import render_news_website,render_stocks
from django.urls import path, include

urlpatterns = [
    path('',render_news_website),
    path('stocks',render_stocks)
]
