from django.shortcuts import render, HttpResponse

# Create your views here.
def todo_main(request):
    return HttpResponse("Todo List")

def todo_home(request):
    return HttpResponse("Home")