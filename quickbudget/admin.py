from django.contrib import admin

from quickbudget.models import Budget, Category, Expense

admin.site.register(Budget)
admin.site.register(Category)
admin.site.register(Expense)
