from django.urls import path
from .views import users, register, login, AuthenticateUser, logout, PermissionAPIView, RoleViewSet

urlpatterns = [
    path("users", users),
    path("register", register),
    path("login", login),
    path("logout", logout),
    path("user", AuthenticateUser.as_view()),
    path("permissions", PermissionAPIView.as_view()),
    path("roles", RoleViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
    path("roles/<str:pk>", RoleViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy',
    })),
]
