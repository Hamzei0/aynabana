from django.urls import path
from . import views

urlpatterns = [
    path("", views.Services.as_view(), name="services"),
]
