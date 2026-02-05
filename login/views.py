from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, TaskForm
from .models import Task
from django.contrib.auth.models import User

def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            return render(request, "register.html", {
                "error": "Username already exists"
            })

        User.objects.create_user(
            username=username,
            password=password
        )

        return redirect("login")  # IMPORTANT

    return render(request, "register.html")

# Register
# def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect("dashboard")
    return render(request, "register.html", {"form": form})

# Login
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            return render(
                request,
                "login.html",
                {"error": "Invalid username or password"}
            )

    return render(request, "login.html")


# Logout
def logout_view(request):
    logout(request)
    return redirect("login")

# Dashboard (Read)
@login_required(login_url='/login/')
def dashboard(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, "dashboard.html", {"tasks": tasks})

# Create
@login_required
def create_task(request):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        task = form.save(commit=False)
        task.user = request.user
        task.save()
        return redirect("dashboard")
    return render(request, "task_form.html", {"form": form})

# Update
@login_required
def update_task(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)
    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect("dashboard")
    return render(request, "task_form.html", {"form": form})

# Delete
@login_required
def delete_task(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)
    task.delete()
    return redirect("dashboard")
