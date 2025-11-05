from django.urls import path
from . import views

urlpatterns = [
    path('news/', views.news_page, name='news_page'),
    path('jokes/', views.jokes_page, name='jokes_page'),
]
