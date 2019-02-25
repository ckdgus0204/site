from django.shortcuts import render,get_object_or_404,redirect
from present.models import Present
from .models import Choice

# Create your views here.
def poll(request):
    present_list= Present.objects.all().order_by('choice__votes')
    age=Choice.PRESENT_CHOICES
    content = {'present':present_list}
    return render(request,'poll.html',{'presents':present_list})

def new(request):
    present=Present.objects.filter(title=request.GET['present'])

    presents=Choice.objects.filter(age=request.GET['age']).order_by('votes')

    if present.first() in presents:
        presents.votes+1
        
    else:
        choice=Choice()
        choice.poll=present.first()
        choice.age=request.GET['age']
        choice.save()
    
    return redirect('home')