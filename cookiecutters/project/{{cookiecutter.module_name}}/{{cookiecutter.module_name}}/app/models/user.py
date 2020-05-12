from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from {{cookiecutter.module_name}}.app.managers import UserManager
from {{cookiecutter.module_name}}.app.mixins import ModelMixin


class User(ModelMixin, AbstractBaseUser, PermissionsMixin):
    class Meta:
        app_label = "app"
        db_table = "users"
        ordering = ("created_at",)
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        abstract = False

    email = models.EmailField(verbose_name=_("Email"), unique=True)
    password = models.CharField(verbose_name=_("Password"), max_length=128)
    name = models.CharField(verbose_name=_("Name"), max_length=150)
    is_active = models.BooleanField(verbose_name=_("Is active?"), default=False)
    is_superuser = models.BooleanField(verbose_name=_("Is superuser?"), default=False)
    is_staff = models.BooleanField(verbose_name=_("Is staff?"), default=False)

    def __str__(self):
        return self.name

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "name",
        "password",
    ]
