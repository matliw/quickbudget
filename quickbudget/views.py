from rest_framework import generics

from quickbudget.api.permissions import BudgetMembersOnly, \
    AllBudgetExpenseMembersOnly, BudgetExpenseMembersOnly
from quickbudget.api.serializers import ExpenseSerializer, \
    CategoriesSerializer, BudgetSerializer
from quickbudget.models import Budget, Expense, Category


class ListAddBudgets(generics.ListCreateAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer

    def perform_create(self, serializer):
        return serializer.save(members=[self.request.user])


class BudgetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
    lookup_url_kwarg = "budget_id"
    permission_classes = [AllBudgetExpenseMembersOnly]


class AddExpenses(generics.CreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [BudgetExpenseMembersOnly]


class ExpenseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    lookup_url_kwarg = "expense_id"


class ListCategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer
