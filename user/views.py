from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import (
  CreateView
)
from django.contrib.auth.views import (
  LoginView,
  LogoutView
)
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
class UserLoginView(LoginView):
  model = User
  template_name = "user/user_login.html"

  def get(self, request, *args, **kwargs):
    if request.user.is_authenticated:
      return redirect('kontak:daftar_kontak')
    return super().get(request, *args, **kwargs)

  def get_success_url(self, *args, **kwargs):
    return reverse_lazy('kontak:daftar_kontak')

class UserRegisterView(CreateView):
  model = User
  form_class = UserCreationForm
  template_name = "user/user_register.html"

  def get(self, request, *args, **kwargs):
    if request.user.is_authenticated:
      return redirect('kontak:daftar_kontak')
    return super().get(request, *args, **kwargs)

  def get_success_url(self, *args, **kwargs):
    return reverse_lazy('user:user_login')

class UserLogoutView(LogoutView):
  model = User
  template_name = 'user/user_logout_success.html'