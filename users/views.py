from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import UserCreateForm

@login_required
def profile(request):
  return render(request, "profile.html")

def user_create(request):
  if request.method == "POST":
    form = UserCreateForm(request.POST)
    if form.is_valid():
      form.save()
      # username = form.cleaned_data.get("username")
      messages.success(
        request, "Your account has been created. You can now login"
      )
      return redirect("/login")
  else:
    form = UserCreateForm()
    return render(request, "users/create.html", {"form": form})

def user_login(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)

    if user is not None:
      login(request, user)
      messages.success(request, 'Login successful.')
      return redirect('/')
    else:
      messages.error(request, 'Invalid username or password.')
      return redirect('/login')
      # return render(request, 'login.html')
  else:
    return render(request, 'users/login.html')

def user_logout(request):
  logout(request)
  messages.success(request, 'Logout successful')
  return redirect('/')
