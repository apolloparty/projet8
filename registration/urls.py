from django.urls import path
from .views import register, myaccount, register2, myaccount2, disconect, client

urlpatterns = [
    path('register', register, name = 'register'),
    path('myaccount', myaccount, name = 'myaccount'),
    path('register2', register2, name = 'register2'),
    path('myaccount2', myaccount2, name = 'myaccount2'),
    path('disconect', disconect, name = 'disconect'),
    path('client', client, name = 'client'),
]