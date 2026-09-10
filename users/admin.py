from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    ordering = ("email",)
    list_display = ("email", "is_superuser", "is_active")
    list_filter = ("email", "is_superuser", "is_active")

    search_fields = ("email",)

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "username",
                    "is_staff",
                    "is_active",
                    "is_superuser",
                ),
            },
        ),
    )
    fieldsets = (
        (
            "Authentication",
            {
                "fields": ("email", "password", "username"),
            },
        ),
        (
            "Permission",
            {
                "fields": (
                    "is_staff",
                    "is_active",
                    "is_superuser",
                )
            },
        ),
    )


admin.site.register(CustomUser, CustomUserAdmin)
