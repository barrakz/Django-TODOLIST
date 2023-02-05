from django.shortcuts import render, redirect
from .models import Task, Category


# MAIN MENU AND TASKS ADD AND EDIT

def index(request):
    print(request.GET)
    tasks = Task.objects.all().order_by('-created_at')
    categories = Category.objects.all()
    status = request.GET.get('status')
    if status == "True":
        tasks = tasks.filter(completed=True)
    elif status == "False":
        tasks = tasks.filter(completed=False)

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


# CATEGORIES

def add_category(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        Category.objects.create(name=name)
        return redirect('add_category')
    context = {'categories': categories}
    return render(request, 'tasks/add_category.html', context)


def edit_category(request, pk):
    category = Category.objects.get(id=pk)
    if request.method == 'POST':
        category.name = request.POST['name']
        category.save()
        return redirect('add_category')
    context = {'category': category}
    return render(request, 'tasks/edit_category.html', context)


def delete_category(request, pk):
    try:
        default_category = Category.objects.get(name='None')
    except Category.DoesNotExist:
        default_category = Category.objects.create(name='None')

    default_category = Category.objects.get(name='None')
    tasks = Task.objects.filter(category=pk)
    for task in tasks:
        task.category = default_category
        task.save()
    Category.objects.get(id=pk).delete()
    return redirect('add_category')
