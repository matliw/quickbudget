from rest_framework import permissions

from quickbudget.models import Budget


class BudgetMembersOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        if request.user.id == obj.created_by.id:
            return True

        return False


class IsBudgetOwnerOrSafeMethods(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        if request.user == obj.created_by:
            return True

        if request.user in obj.members.all():  # get, head, options

            return True

        return False


class ExpenseBudgetMembersOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        if request.user in obj.budget.members.all():
            return True

        return False


class AllBudgetExpenseMembersOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True

        current_budget = Budget.objects.get(pk=view.kwargs.get("budget_id"))
        if request.user in current_budget.members.all():
            return True

        return False


class IsPostOrIsAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        """allow POST method without authentication"""
        if request.method == "POST":
            return True

        return request.user and request.user.is_authenticated
