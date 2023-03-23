import datetime
import uuid

from django.db import models


class Budget(models.Model):
    budget_id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                                 editable=False, unique=True)
    name = models.CharField(max_length=120)
    monthly_limit = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    created_timestamp = models.TimeField(auto_now_add=True)
    members = models.ManyToManyField("auth.User")

    def __str__(self):
        return f"{self.name}"


class Category(models.Model):
    category_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=120)
    description = models.TextField(max_length=250)

    def __str__(self):
        return f"{self.name}"


class Expense(models.Model):
    expense_id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                                  editable=False, unique=True)
    name = models.CharField(max_length=120)
    total = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    budget = models.ForeignKey(Budget, null=False, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, null=True,
                                 on_delete=models.SET_NULL)
    created_timestamp = models.TimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"
