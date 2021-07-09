from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import TodoListItem
# Create your views here.
def todoappView(request):
    items = TodoListItem.objects.all()
    return render(request, 'todolist.html', {'all_items': items})

def addTodoView(request):
    x = request.POST['content']
    new_item = TodoListItem(content=x)
    new_item.save()
    return HttpResponseRedirect('/todoapp/')

def deleteTodoView(request, i):
    x = TodoListItem.objects.get(id=i)
    x.delete()
    return HttpResponseRedirect('/todoapp/')
