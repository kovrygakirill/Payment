import uuid

from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    tin = models.UUIDField(default=uuid.uuid4, unique=True, editable=False,
                           verbose_name="Идентификационный номер налогоплательщика")
    balance = models.DecimalField(max_digits=12, decimal_places=2)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')

    class Meta:
        db_table = "user_profile"

    def __str__(self):
        return str(self.user)
