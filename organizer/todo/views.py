from django.shortcuts import render, HttpResponse

# Create your views here.

todos = [
    {'content':"Do stuff"},
    {'content':"Do more stuff"}
]

def todo_main(request):
    return HttpResponse("Todo List")

def todo_home(request):
    context = {
        'todos':todos
    }
    return render(request, "todo/todo_list.html", context)