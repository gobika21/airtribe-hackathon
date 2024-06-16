from .views import render_news_website
from django.urls import path, include

urlpatterns = [
    path('',render_news_website),
    ]
