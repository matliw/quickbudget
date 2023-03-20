from rest_framework import serializers
from quickbudget.models import Budget, BudgetUsers, Expense, Category, UserRole


class BudgetUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BudgetUsers
        fields = ['user_id', 'first_name', 'last_name']


class BudgetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Budget
        fields = ['budget_id', 'name', 'monthly_limit', 'description',
                  'created_by', 'created_timestamp']


class UserRoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserRole
        fields = ['budget_id', 'user_id', 'user_role']


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['category_id', 'name', 'description']


class ExpenseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Expense
        fields = ['expense_id', 'name', 'total', 'description',
                  'budget', 'created_by', 'created', 'category',
                  'created_timestamp']
