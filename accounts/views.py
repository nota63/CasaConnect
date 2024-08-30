from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.shortcuts import render,redirect


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account created successfully')
            return redirect('login')
    else:
        form=UserCreationForm()
    return render(request, 'accounts/signup.html',{'form':form})


def login_view(request):
    if request. method == 'POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request, user)
            messages.success(request,'Logged in successfully')
            return redirect('home')
    else:
        form=AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request,'logged out successfully')
        return redirect('home')
    return render(request,'accounts/logout.html')

