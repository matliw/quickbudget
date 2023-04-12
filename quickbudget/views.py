from rest_framework import generics

from quickbudget.api.serializers import ExpenseSerializer, \
    CategoriesSerializer, BudgetSerializer
from quickbudget.models import Budget, Expense, Category


class ListAddBudgets(generics.ListCreateAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer  # without expenses


class BudgetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
    lookup_url_kwarg = "budget_id"


class AddExpenses(generics.CreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer


class ExpenseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    lookup_url_kwarg = "expense_id"


class ListCategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer
