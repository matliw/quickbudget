import uuid

from _decimal import Decimal
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from core import settings


class Budget(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                                 editable=False)
    name = models.CharField(max_length=120)
    budget_limit = models.DecimalField(max_digits=8, decimal_places=2, null=True, validators=[MinValueValidator(Decimal('0.01'))])
    description = models.CharField(max_length=200, null=True, blank=True)
    created_timestamp = models.DateTimeField(auto_now=True)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL)
    last_interaction = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=120)
    description = models.TextField(max_length=250, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"


class Expense(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=120)
    total = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    description = models.CharField(max_length=200, null=True, blank=True)
    budget_id = models.ForeignKey(Budget, on_delete=models.CASCADE, related_name="expenses")
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    created_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"


class User(AbstractUser):

    def __str__(self):
        return f"{self.username}"
