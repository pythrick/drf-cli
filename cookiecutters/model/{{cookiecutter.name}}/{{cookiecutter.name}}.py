from django.db import models
from django.utils.translation import gettext_lazy as _
from ..mixins import ModelMixin


class {{cookiecutter.class_name}}(ModelMixin):
    class Meta:
        app_label = "{{cookiecutter.app_name}}"
        db_table = "{{cookiecutter.table_name}}"
        ordering = ("created_at",)
        verbose_name = _("{{cookiecutter.class_name}}")
        verbose_name_plural = _("{{cookiecutter.class_name_plural}}")
        abstract = False
