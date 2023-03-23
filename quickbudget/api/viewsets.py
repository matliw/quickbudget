from rest_framework.viewsets import ModelViewSet

from quickbudget.api.serializers import BudgetSerializer, CategorySerializer, ExpenseSerializer
from quickbudget.models import Budget, Category, Expense


class BudgetViewSet(ModelViewSet):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ExpenseViewSet(ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
