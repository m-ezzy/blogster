from django.shortcuts import redirect, render
# from django.core.urlresolvers import reverse_lazy
from django.views.generic import UpdateView
from django.contrib.auth import get_user_model
# from .forms import UserEditMultiForm

User = get_user_model()

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
