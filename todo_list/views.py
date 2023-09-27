
from django.shortcuts import render, redirect
from django.contrib import messages

# import todo form and models

from .forms import TodoForm
from .models import Todo

def index(request):

    item_list = Todo.objects.order_by("-date")
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todos')
    form = TodoForm()

    page = {
        "forms": form,
        "list": item_list,
        "title": "TODO LIST",
        "analytics": get_todos_length(request)
    }
    return render(request, 'todo/todo.html', page)

### function to remove item, it receive todo item_id as primary key from url ##
def remove(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect('todos')

def changeStatus(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.status = not item.status
    item.save()
    return redirect('todos')

def get_todos_length(request):
    todos = Todo.objects.all()
    todos_length = todos.count()
    completed_todos = todos.filter(status=True).count()
    pending_todos = todos_length - completed_todos

    return {
            'todos_length': todos_length,
            'completed_todos': completed_todos,
            'pending_todos': pending_todos
            }