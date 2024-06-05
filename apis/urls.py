from .views import create_user, create_note, get_notes, edit_note, delete_note
from django.urls import path

urlpatterns = [
    path("create_user", create_user, name="create_user"),
    path("create_note", create_note, name="create_note"),
    path("get_notes", get_notes, name="get_notes"),
    path("edit_note", edit_note, name="edit_note"),
    path("delete_note", delete_note, name="delete_note")
]
