from django.urls import path
from myportfolio import views                           #take care this line
urlpatterns = [
    path('', views.index, name='index'),                       
    path('contact', views.contact, name='contact'),                                              
]

