from django.urls import path, include
from .views import worker_list, worker_detail

app_name = "accounts"

urlpatterns = [
    path("workers/", worker_list, name="worker_list"),
    path("workers/<int:pk>/", worker_detail, name="worker_detail"),
    path("", include("django.contrib.auth.urls")),
]
