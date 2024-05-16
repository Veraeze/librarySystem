from django.contrib import admin
from .models import LibraryUser
from django.contrib.auth.admin import UserAdmin


# Register your models here.
@admin.register(LibraryUser)
class LibraryUserAdmin(UserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2", "first_name", "last_name"),
            },
        ),
    )
