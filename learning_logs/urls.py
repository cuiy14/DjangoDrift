"""define the url mode of the app learning_logs"""
from django.conf.urls import url

from . import views

urlpatterns = [
    #main pages
    url(r'^$',views.index,name='index'),
    #show all the topics
    url(r'^topics/$', views.topics, name='topics'),
    #show the detailed page about a specific topic
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    #the page for adding new topic
    url(r'^new_topic/$',views.new_topic, name='new_topic'),
    #the page for adding new items
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    #the page for editing entry
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]
