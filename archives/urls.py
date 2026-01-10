from django.urls import path

from . import views

urlpatterns = [
    path("", views.ArchivesListView.as_view(), name="archive_list"),
]
