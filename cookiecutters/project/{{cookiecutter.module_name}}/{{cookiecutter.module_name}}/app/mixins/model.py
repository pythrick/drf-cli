import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class ModelMixin(models.Model):
    class Meta:
        abstract = True

    id = models.UUIDField(
        verbose_name=_("Id"),
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True,
    )

    created_at = models.DateTimeField(
        verbose_name=_("Created at"),
        auto_now_add=True,
        null=False,
        blank=False,
        help_text=_("Creation datetime"),
    )

    updated_at = models.DateTimeField(
        verbose_name=_("Updated at"),
        auto_now=True,
        null=True,
        blank=False,
        help_text=_("Update datetime"),
    )
