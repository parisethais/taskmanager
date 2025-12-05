from django.urls import path
from django.contrib.auth.views import LoginView
from .views import worker_list, worker_detail, logout_view

app_name = "accounts"

urlpatterns = [
    path(
        "login/",
        LoginView.as_view(template_name="registration/login.html"),
        name="login",
    ),
    path("logout/", logout_view, name="logout"),
    path("workers/", worker_list, name="worker_list"),
    path("workers/<int:pk>/", worker_detail, name="worker_detail"),
]
