from django.shortcuts import render

# Create your views here.
def todoappView(request):
    return render(request, 'todolist.html')