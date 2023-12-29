from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import UserLoginForm, UserCreateForm, UserEditForm

def login_user(request):
  if request.method == 'GET':
    if request.user.is_authenticated:
      return redirect('/')
    else:
      form = UserLoginForm()
      return render(request, 'login.html', {'form': form})
  elif request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)

    if user is None:
      messages.error(request, 'Invalid username or password.')
      return redirect('/login')
      # return render(request, 'login.html')
    else:
      login(request, user)
      messages.success(request, 'Login successful.')
      return redirect('/')

@login_required
def logout_user(request):
  if request.method == 'POST':
    logout(request)
    messages.success(request, 'Logout successful')
    return redirect('/')

#####################################################################################################################################

def display_user(request, id):
  user = User.objects.get(pk=id)
  context = {
    "user": user,
  }
  return render(request, "users/user.html", context)

def create_user(request): # user_create # register # signup
  if request.method == "GET":
    if request.user.is_authenticated:
      return redirect("/")
    else:
      form = UserCreateForm()
      return render(request, "users/create.html", {"form": form})
  else:
    form = UserCreateForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, "Your account has been created. You can now login")

      # username = form.cleaned_data.get("username")
      # password = form.cleaned_data.get("password1")
      # user = authenticate(request, username=username, password=password)
      return redirect("/login")

@login_required
def edit_user(request, id):
  user = User.objects.get(pk=id)
  if request.method == 'GET':
    form = UserEditForm(instance=user)
    return render(request, "users/edit.html", {"form": form})
  elif request.method == 'POST':
    form = UserEditForm(request.POST, instance=user)
    if form.is_valid():
      form.save()
      messages.success(request, 'User updated.')
      return redirect('/account')

@login_required
def delete_user(request, id):
  if request.method == 'POST':
    logout(request)
    User.objects.get(pk=id).delete()
    messages.success(request, 'User deleted.')
    return redirect('/')

#####################################################################################################################################

@login_required
def account(request): # account # profile
  if request.method == 'GET':
    # form = UserDeleteForm(instance=request.user)
    # form = UserLogoutForm(instance=request.user)
    return render(request, "account.html")


