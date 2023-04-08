from django.contrib.auth.models import User
from rest_framework import serializers
from quickbudget.models import Budget, Expense, Category


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']
        read_only_fields = ('id',)


class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = ['id', 'name', 'budget_limit', 'description', 'created_timestamp']

        read_only_fields = ('budget_id', 'created_timestamp')

        def create(self, validated_data, **kwargs):
            validated_data['id'] = \
            self.context['request'].parser_context['kwargs']['expense']
            return super(ExpenseSerializer, self).create(validated_data)


class BudgetListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = ['name', 'description', 'created_timestamp']

        read_only_fields = ('created_timestamp',)


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'description']


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ['id', 'name', 'total', 'description', 'budget_id', 'category', 'created_timestamp']
        read_only_fields = ('id', 'created_timestamp',)

        def create(self, validated_data, **kwargs):
            validated_data['id'] = \
            self.context['request'].parser_context['kwargs']['expense']
            return super(ExpenseSerializer, self).create(validated_data)


class ExpenseListSerializer(serializers.ModelSerializer):
    expense_items = ExpenseSerializer(many=True, read_only=True)
    # members = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Budget
        fields = ['name', 'expense_items']


class ExpensesByCategoriesSerializer(serializers.ModelSerializer):
    categories = CategoriesSerializer(many=True, read_only=True)
    expense_items = ExpenseSerializer(many=True, read_only=True)

    class Meta:
        model = Expense
        fields = ['categories', 'expense_items']