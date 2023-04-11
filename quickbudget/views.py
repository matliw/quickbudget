from rest_framework import generics

from quickbudget.api.serializers import ExpenseSerializer, \
    CategoriesSerializer, BudgetListSerializer
from quickbudget.models import Budget, Expense, Category


class ListAddBudgets(generics.ListCreateAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetListSerializer  # without expenses


class BudgetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetListSerializer
    lookup_url_kwarg = "budget_id"


class ListAddExpensesList(generics.ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer


class ExpenseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    lookup_url_kwarg = "expense_id"

    # def perform_create(self, serializer):
    #     return serializer.save(members=[self.request.user])


class ListCategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer
