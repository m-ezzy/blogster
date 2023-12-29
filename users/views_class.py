from django.shortcuts import redirect, render
# from django.core.urlresolvers import reverse_lazy
from django.views.generic import UpdateView
from django.contrib.auth import get_user_model
# from .forms import UserEditMultiForm
from .views import LoginView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm

User = get_user_model()



class UserLoginView(LoginView):
  template_name = 'users/login.html'
  form_class = AuthenticationForm
  success_url = '/'
  redirect_authenticated_user = True

  def get_success_url(self):
    return self.success_url
  
  def form_valid(self, form):
    messages.success(self.request, 'Login successful.')
    return super().form_valid(form)
  
  def form_invalid(self, form):
    messages.error(self.request, 'Invalid username or password.')
    return super().form_invalid(form)
  
  def get(self, request, *args, **kwargs):
    if request.user.is_authenticated:
      return redirect('/')
    return super().get(request, *args, **kwargs)
  
  def post(self, request, *args, **kwargs):
    if request.user.is_authenticated:
      return redirect('/')
    return super().post(request, *args, **kwargs)


class UserLoginView(UpdateView):
  model = User
  # form_class = UserLoginForm
  # success_url = reverse_lazy('home')

  def form_valid(self, form):
    login(self.request, form.get_user())
    return redirect('home')

class UserSignupView(UpdateView):
  model = User
  # form_class = UserEditMultiForm
  # success_url = reverse_lazy('home')

  def get_form_kwargs(self):
    kwargs = super(UserSignupView, self).get_form_kwargs()
    kwargs.update(instance={
      'user': self.object,
      'profile': self.object.profile,
    })
    return kwargs
