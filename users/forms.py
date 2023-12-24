from django.forms import ModelForm
# from betterforms.multiform import MultiModelForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from .models import UserProfile

User = get_user_model()

class UserCreateForm(UserCreationForm):
  class Meta:
    model = User
    fields = ('username', 'email', 'password1', 'password2',)

class UserEditForm(UserChangeForm):
  class Meta:
    fields = ('email',)

class UserProfileForm(ModelForm):
  class Meta:
    fields = ('favorite_color',)

# class UserEditMultiForm(MultiModelForm):
#   form_classes = {
#     'user': UserEditForm,
#     'profile': UserProfileForm,
#   }
