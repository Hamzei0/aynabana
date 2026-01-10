from django import forms

from . import models


class ArchiveCommentForm(forms.ModelForm):
    class Meta:
        model = models.CommentArchive
        fields = ["text", "stars"]
