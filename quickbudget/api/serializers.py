from django.contrib.auth.models import User
from rest_framework import serializers
from quickbudget.models import Budget, Expense, Category


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']
        read_only_fields = ('id',)


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ['id', 'name', 'total', 'description', 'category']
        read_only_fields = ('id', 'created_timestamp',)

        def create(self, validated_data, **kwargs):
            validated_data['budget_id'] = \
            self.context['request'].parser_context['kwargs']['budget_id']
            return super(ExpenseSerializer, self).create(validated_data)


class BudgetSerializer(serializers.ModelSerializer):
    expenses = ExpenseSerializer(many=True, read_only=True)

    class Meta:
        model = Budget
        fields = ['id', 'name', 'budget_limit', 'description', 'created_timestamp', 'expenses']

        read_only_fields = ('budget_id', 'created_timestamp',)


class BudgetListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = ['id', 'name', 'description', 'budget_limit', 'created_timestamp']

        read_only_fields = ('created_timestamp',)


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'description']


class ExpenseListSerializer(serializers.ModelSerializer):
    expenses = ExpenseSerializer(many=True, read_only=True)
    # members = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Budget
        fields = ['id', 'name', 'expenses']
