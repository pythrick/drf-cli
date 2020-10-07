from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.utils.translation import gettext_lazy as _
from {{cookiecutter.module_name}}.app import models


@admin.register(models.User)
class UserAdmin(auth_admin.UserAdmin):
    list_display = ("name", "email", "created_at")
    readonly_fields = ("id", "last_login", "created_at", "updated_at")
    list_filter = ("is_staff", "is_active", "is_superuser")
    search_fields = ("id", "name", "email")
    ordering = ("name",)
    filter_horizontal = ()

    fieldsets = (
        (None, {"fields": ("id", "email", "password")}),
        (_("Personal info"), {"fields": ("name",)}),
        (_("Permissions"), {"fields": ("is_active", "is_staff", "is_superuser"),}),
        (_("Important dates"), {"fields": ("last_login", "created_at", "updated_at")}),
    )
    add_fieldsets = (
        (None, {"classes": ("wide",), "fields": ("email", "password1", "password2"),}),
    )
