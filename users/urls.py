"""define the URL mode for users app"""

from django.conf.urls import url
from django.contrib.auth.views import login

from . import views

urlpatterns = [
    #login page
    url(r'^login/$', login, {'template_name':'users/login.html'}, name='login'),
]