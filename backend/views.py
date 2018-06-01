from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
    return render(request, 'index.html')

def welcome(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        return render(request, 'welcome.html')

def login(request):
    return render(request, 'login.html')


def logout(request):
    return render(request, 'logout.html')
    

def signup(request):
    return render(request, 'signup.html')


def password_reset(request):
    return render(request, 'password_reset.html')
