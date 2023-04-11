from django.contrib import admin

from quickbudget_app.models import Budget, Category, Expense

admin.site.register(Budget)
admin.site.register(Category)
admin.site.register(Expense)
