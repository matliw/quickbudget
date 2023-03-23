from django.contrib.auth.models import User
from rest_framework import serializers
from quickbudget.models import Budget, Expense, Category


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]


class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = ['budget_id', 'name', 'monthly_limit', 'description', 'created_timestamp']
        read_only_fields = ('budget_id',)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_id', 'name', 'description']
        read_only_fields = ('category_id',)


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ['expense_id', 'name', 'total', 'description',
                  'budget', 'category',
                  'created_timestamp']
        read_only_fields = ('expense_id',)

        def create(self, validated_data, **kwargs):
            validated_data['budget_id'] = self.context['request'].parser_context['kwargs']['pk']
            return super(ExpenseSerializer, self).create(validated_data)


class BudgetExpenseListSerializer(serializers.ModelSerializer):
    expense_items = ExpenseSerializer(many=True, read_only=True)
    members = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Budget
        fields = ['budget_id', 'name', 'expense_items', 'members']