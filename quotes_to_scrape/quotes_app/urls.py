from django.urls import path
from . import views
import re

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.sing_in, name='login'),
    path(r'authors/<str:author_name>/', views.authors, name='authors'),
    path('register/', views.sign_up, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('new_author/', views.new_author, name='new_author'),
    path('new_quote/', views.new_quote, name='new_quote'),
    path('authors/', views.authors, name='authors'),
    
]