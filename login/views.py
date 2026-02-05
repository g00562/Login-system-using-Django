from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, TaskForm
from .models import Task


def register_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("dashboard")

    return render(request, "register.html", {"form": form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    error = None

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            error = "Invalid username or password"

    return render(request, "login.html", {"error": error})


@login_required
def logout_view(request):
    logout(request)
    return redirect("login")


@login_required
def dashboard(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, "dashboard.html", {"tasks": tasks})


@login_required
def create_task(request):
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect("dashboard")

    return render(request, "task_form.html", {"form": form})


@login_required
def update_task(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)
    form = TaskForm(instance=task)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            return redirect("dashboard")

    return render(request, "task_form.html", {"form": form})


@login_required
def delete_task(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)

    if request.method == "POST":
        task.delete()
        return redirect("dashboard")

    return render(request, "confirm_delete.html", {"task": task})
