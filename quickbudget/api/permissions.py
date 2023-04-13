from rest_framework import permissions

from quickbudget.models import Budget


class BudgetMembersOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.user.is_superuser:
            return True

        if request.user in obj.members.all():
            return True

        return False


class BudgetExpenseMembersOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.user.is_superuser:
            return True

        if request.user in obj.shopping_list.members.all():
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