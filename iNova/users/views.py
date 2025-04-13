from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,authenticate
from django.contrib.auth import login,logout

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to home after successful registration
    else:
        form = UserCreationForm()  # Ensure form is created for GET request
    return render(request, 'websites/register.html', {'form': form})  # Pass form to template



def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
    return render(request,'websites/login.html')

def user_logout(request):
    logout(request)
    return redirect('home')

def user_home(request):
    return render(request,'websites/home.html')