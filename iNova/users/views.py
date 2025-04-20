from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

# # Register view
# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             return redirect('login')  # Redirect to login page after successful registration
#     else:
#         form = UserCreationForm()
#     return render(request, 'websites/register.html', {'form': form})


# Register view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user
            login(request, user)  # Automatically log in the user after registration
            return redirect('anomaly')  # Redirect to anomaly page (or wherever you want)
    else:
        form = UserCreationForm()
    return render(request, 'websites/register.html', {'form': form})

# Login view
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('anomaly')  # Redirect to home page after successful login
    else:
        form = AuthenticationForm()
    return render(request, 'websites/login.html', {'form': form})


# Home view (after login)
def user_home(request):
    return render(request, 'websites/home.html')

def user_logout(request):
    logout(request)  # Logs out the user
    return redirect('login')  # Redirect to login page after logout
