from rest_framework import generics
from quickbudget.api.serializers import ExpenseSerializer, \
    ExpenseListSerializer, CategoriesSerializer, BudgetSerializer, \
    BudgetListSerializer
from quickbudget.models import Budget, Expense, Category


class ListBudgets(generics.ListCreateAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetListSerializer


class BudgetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer

    def perform_create(self, serializer):
        return serializer.save(members=[self.request.user])


class ListExpensesList(generics.ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseListSerializer


class ExpenseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    lookup_url_kwarg = "expense"

    # def perform_create(self, serializer):
    #     return serializer.save(members=[self.request.user])


class ListCategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer
