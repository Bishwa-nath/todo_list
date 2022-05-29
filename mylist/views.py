from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Tasks

# Create your views here.
def home(request):
    tasks = Tasks.objects.all().values()
    context = {
        'tasks': tasks
    }
    return render(request, 'mylist/index.html', context=context)

def addtasks(request):
    t = request.POST['title']
    d = request.POST['descrip']
    tas = Tasks(title=t, descrip=d)
    tas.save()
    return HttpResponseRedirect(reverse('todo-home'))

def delete(request, id):
    tas = Tasks.objects.get(id=id)
    tas.delete()
    return HttpResponseRedirect(reverse('todo-home'))

def update(request, id):
    tas = Tasks.objects.get(id=id)
    context = {
        'tasks': tas,
    }
    return render(request, 'mylist/update.html', context=context)

def updatetask(request, id):
    t = request.POST['title']
    d = request.POST['descrip']
    tas = Tasks.objects.get(id=id)
    tas.title = t
    tas.descrip = d
    tas.save()
    return HttpResponseRedirect(reverse('todo-home'))