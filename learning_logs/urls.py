"""define the url mode of the app learning_logs"""
from django.conf.urls import url

from . import views

urlpatterns = [
    #main pages
    url(r'^$',views.index,name='index'),
    #show all the topics
    url(r'^topics/$', views.topics, name='topics'),
]
