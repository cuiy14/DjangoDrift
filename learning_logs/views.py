from django.shortcuts import render

# Create your views here.
def index(request):
    """the main page of learing_logs""" 
    return render(request,'learning_logs/index.html')
