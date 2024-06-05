from django.urls import path
from .views import *

urlpatterns = [
    path('', login, name='login'),
    path('login', login, name='login'),
    path('register', register, name='register'),
    path('notes', notes, name='notes')
]
