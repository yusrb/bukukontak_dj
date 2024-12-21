from django.urls import path
from .views import (
  UserLoginView,
  UserRegisterView,
  UserLogoutView,

  # user_logout_success
)

urlpatterns = [
  path('login/', UserLoginView.as_view(), name="user_login"),
  path('register/', UserRegisterView.as_view(), name="user_register"),
  path('logout/', UserLogoutView.as_view(), name="user_logout"),
  # path('logout/success', user_logout_success, name="user_logout_success"),
]