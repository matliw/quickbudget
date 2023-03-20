import datetime
import uuid
from django.db import models


class BudgetUsers(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)


class Budget(models.Model):
    budget_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=120)
    monthly_limit = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    created_by = models.ForeignKey(BudgetUsers, on_delete=models.SET_NULL, null=True)
    created_timestamp = models.TimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_timestamp']


class UserRole(models.Model):
    ROLE_CHOICES = [
        ('r', 'read'),
        ('w', 'write'),
        ('a', 'admin')
    ]
    budget_id = models.ForeignKey(Budget, on_delete=models.CASCADE)
    user_id = models.ForeignKey(BudgetUsers, on_delete=models.CASCADE)
    user_role = models.CharField(max_length=2, choices=ROLE_CHOICES, default='read')


class Category(models.Model):
    category_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=120)
    description = models.TextField(max_length=250)


class Expense(models.Model):
    expense_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=120)
    total = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    budget = models.ForeignKey(Budget, null=False, on_delete=models.CASCADE)
    created_by = models.ForeignKey(BudgetUsers, null=True, on_delete=models.SET_NULL)
    created = models.TimeField(datetime.date.today, null=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    created_timestamp = models.TimeField()

