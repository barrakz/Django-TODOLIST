from django.contrib.auth import logout, login
from django.shortcuts import render, redirect

from taskapp import settings
from .models import Task, Category
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


# MAIN MENU AND TASKS ADD AND EDIT
@login_required(login_url=settings.LOGIN_URL)
def index(request):
    tasks = Task.objects.filter(user=request.user).order_by('-created_at')
    categories = Category.objects.filter(user=request.user)
    status = request.GET.get('status')
    if status == "True":
        tasks = tasks.filter(completed=True)
    elif status == "False":
        tasks = tasks.filter(completed=False)

    context = {'tasks': tasks, 'categories': categories, 'user': request.user}
    return render(request, 'tasks/index.html', context)


@login_required
def add(request):
    categories = Category.objects.filter(user=request.user)
    if request.method == 'POST':
        name = request.POST['name']
        category = Category.objects.get(id=request.POST['category'])
        Task.objects.create(name=name, category=category, user=request.user)
        return redirect('index')
    context = {'categories': categories}
    return render(request, 'tasks/add.html', context)


@login_required
def edit(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        task.name = request.POST['name']
        task.save()
        return redirect('index')
    context = {'task': task}
    return render(request, 'tasks/edit.html', context)


@login_required
def delete(request, pk):
    Task.objects.get(id=pk).delete()
    return redirect('index')


@login_required
def complete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.completed = request.POST.get('completed', False) == 'on'
    task.save()
    return redirect('index')


# CATEGORIES
@login_required
def add_category(request):
    if request.method == 'POST':
        name = request.POST['name']
        Category.objects.create(name=name, user=request.user)
        return redirect('add_category')
    categories = Category.objects.filter(user=request.user)
    context = {'categories': categories}
    return render(request, 'tasks/add_category.html', context)


@login_required
def edit_category(request, pk):
    category = Category.objects.get(id=pk)
    if category.user != request.user:
        return redirect('index')
    if request.method == 'POST':
        category.name = request.POST['name']
        category.save()
        return redirect('add_category')
    context = {'category': category}
    return render(request, 'tasks/edit_category.html', context)


@login_required
def delete_category(request, pk):
    try:
        category = Category.objects.get(id=pk, user=request.user)
        default_category, created = Category.objects.get_or_create(
            name='None', user=request.user)
    except Category.DoesNotExist:
        return redirect('add_category')
    tasks = Task.objects.filter(category=category)
    tasks.update(category=default_category)

    category.delete()
    return redirect('add_category')


from django.shortcuts import redirect

# ...

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log the user in
            login(request, form.get_user())
            return redirect('index') # przekierowanie na stronę główną
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})



def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


def user_not_authenticated(user):
    return not user.is_authenticated
