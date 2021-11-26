from django.shortcuts import render, redirect
from .models import Todo
from .forms import TaskForm


def index(request):
    tasks = Todo.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, 'Todo/index.html', context)


def update(request, id):
    task = Todo.objects.get(id=id)
    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'Todo/update.html', {'form': form})


def add(request):
    if request.method == 'POST':
        todo = request.POST.get('todo')
        Todo.objects.create(task_name=todo)
        return redirect('index')


def delete(request, id):
    task = Todo.objects.get(id=id)
    if request.method == 'POST':
        tasks = Todo.objects.all()
        context = {
            'message': task.task_name + " has been removed.",
            'tasks': tasks
        }
        task.delete()
        return render(request, 'Todo/index.html', context)
    else:
        context = {
            'task': task
        }
        return render(request, 'Todo/delete.html', context)


def complete_task(request, id):
    task = Todo.objects.get(id=id)
    tasks = Todo.objects.all()
    if task.completed:
        task.completed = False
        context = {
            'tasks': tasks
        }
    else:
        task.completed = True
        context = {
            'message': task.task_name + " has been completed.",
            'tasks': tasks
        }
    task.save()
    # return redirect('index')
    return render(request, 'Todo/index.html', context)
