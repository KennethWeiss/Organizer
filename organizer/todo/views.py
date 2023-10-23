from django.shortcuts import render, HttpResponse

# Create your views here.
def todo_main(request):
    return HttpResponse("Todo List")

def home(request):
    return HttpResponse("Home")