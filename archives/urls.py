from django.urls import path

from . import views

urlpatterns = [
    path("", views.ArchivesListView.as_view(), name="archive_list"),
    path("<int:pk>/", views.ArchiveDetailView.as_view(), name="archive_detail"),
    path(
        "comment_create/<int:archive_id>/",
        views.ArchiveCommentCreate.as_view(),
        name="archive_comment_create",
    ),
]
