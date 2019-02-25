from django.shortcuts import render
from .models import Present
from poll.models import Choice
# Create your views here.

def home(request):
    presents=Present.objects.all().order_by('choice__votes')
    
    return render(request,'home.html',{'presents':presents})

def about(request):
    return render(request,'about.html')

def rank(request):
    ages=request.GET['age']
    presents=Choice.objects.filter(age=ages).order_by('votes')
    return render(request, 'rank.html',{
        'presents':presents,
    })