from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import logout


# Create your views here.
def logout_view(request):
    """log out"""
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))
