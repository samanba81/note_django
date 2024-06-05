from django.db.models.functions import Lower
from apis.models import Note, User
from django.contrib import admin


# Register your models here.
@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_filter = ['noteConnect']

    def get_ordering(self, request):
        return [Lower('noteId')]


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
