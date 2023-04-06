import datetime
import uuid

from django.db import models


class Budget(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                                 editable=False)
    name = models.CharField(max_length=120)
    monthly_limit = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.CharField(max_length=200)
    created_timestamp = models.DateTimeField(auto_now=True)
    members = models.ManyToManyField("auth.User")

    def __str__(self):
        return f"{self.name}"


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=120)
    description = models.TextField(max_length=250)

    def __str__(self):
        return f"{self.name}"


class Expense(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          editable=False)
    name = models.CharField(max_length=120)
    total = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.CharField(max_length=200)
    budget_id = models.ForeignKey(Budget, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, null=True,
                                 on_delete=models.SET_NULL)
    created_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"
