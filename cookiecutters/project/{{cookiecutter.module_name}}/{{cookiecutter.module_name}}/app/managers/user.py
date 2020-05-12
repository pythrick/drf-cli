from django.contrib.auth.base_user import BaseUserManager
from django.db import transaction


class UserManager(BaseUserManager):
    @transaction.atomic
    def create_user(self, name: str, email: str, password: str, **kwargs):
        user = self.model(name=name, email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user

    @transaction.atomic
    def create_superuser(self, name, email, password, **kwargs):
        user = self.create_user(name, email, password, **kwargs)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user
