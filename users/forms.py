# from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm

# from .models import UserProfile
from django.forms import ModelForm, CharField, TextInput, EmailInput, PasswordInput

# User = get_user_model()

class UserLoginForm(AuthenticationForm):
  username = CharField(
    label="Username",
    widget=TextInput(attrs={'autofocus': True, 'class': 'form-control'}),
  )
  password = CharField(
    label="Password",
    widget=PasswordInput(attrs={'class': 'form-control'}),
  )
  
  class Meta:
    model = User
    fields = ('username', 'password')
    widgets = {
      # 'username': TextInput(attrs={'class': 'form-control'}),
      # 'password': PasswordInput(attrs={'class': 'form-control bg-danger'}),
    }

class UserCreateForm(UserCreationForm):
  # email = forms.EmailField(required=True)
  
  password1 = CharField(
    label="Password",
    widget=PasswordInput(attrs={'class': 'form-control'}),
  )
  password2 = CharField(
    label="Confirm password",
    widget=PasswordInput(attrs={'class': 'form-control'}),
  )
  
  class Meta:
    model = User
    fields = ('username', 'email', 'password1', 'password2')
    widgets = {
      'username': TextInput(attrs={'class': 'form-control'}),
      'email': EmailInput(attrs={'class': 'form-control'}),
      # 'password1': PasswordInput(attrs={'class': 'form-control'}),
      # 'password2': PasswordInput(attrs={'class': 'form-control'}),
    }
    
    # def save(self, commit=True):
    #   user = super(UserCreateForm, self).save(commit=False)
    #   user.email = self.cleaned_data['email']
    #   if commit:
    #     user.save()
    #   return user

class UserEditForm(UserChangeForm):
  class Meta:
    model = User
    fields = ('username', 'email', 'first_name', 'last_name')
    widgets = {
      'username': TextInput(attrs={'class': 'form-control'}),
      'email': EmailInput(attrs={'class': 'form-control'}),
      'first_name': TextInput(attrs={'class': 'form-control'}),
      'last_name': TextInput(attrs={'class': 'form-control'}),
    }

class UserProfileForm(ModelForm):
  class Meta:
    fields = ('favorite_color',)
