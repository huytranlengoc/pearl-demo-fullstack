from django.urls import path
from .views import users, register, login, AuthenticateUser, logout

urlpatterns = [
    path("users", users),
    path("register", register),
    path("login", login),
    path("logout", logout),
    path("user", AuthenticateUser.as_view()),
]
