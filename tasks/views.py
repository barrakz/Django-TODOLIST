from django.shortcuts import render, redirect
from .models import Task, Category


def index(request):
    tasks = Task.objects.all()
    categories = Category.objects.all()
    context = {'tasks': tasks,
               'categories': categories}
    return render(request, 'tasks/index.html', context)


def add(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        category = Category.objects.get(id=request.POST['category'])
        Task.objects.create(name=name, category=category)
        return redirect('index')
    context = {'categories': categories}
    return render(request, 'tasks/add.html', context)



def edit(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        task.name = request.POST['name']
        task.save()
        return redirect('index')
    context = {'task': task}
    return render(request, 'tasks/edit.html', context)


def delete(request, pk):
    Task.objects.get(id=pk).delete()
    return redirect('index')


def complete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.completed = request.POST.get('completed', False) == 'on'
    task.save()
    return redirect('index')


def add_category(request):
    if request.method == 'POST':
        name = request.POST['name']
        Category.objects.create(name=name)
        return redirect('index')
    return render(request, 'tasks/add_category.html')





