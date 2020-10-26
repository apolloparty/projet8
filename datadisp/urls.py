from django.urls import path
from .views import datadisp, home, contact, saved, myfood, substitutes

urlpatterns = [
    path('', home, name = 'home'),
    path('datadisp', datadisp, name = 'datadisp'),
    path('contact', contact, name = 'contact'),
    path('saved', saved, name = 'saved'),
    path('myfood', myfood, name = 'myfood'),
    path('substitutes', substitutes, name = 'substitutes'),
]
