from rest_framework import generics
from quickbudget.api.serializers import ExpenseSerializer, \
    BudgetExpenseListSerializer, CategoriesSerializer, BudgetSerializer, \
    BudgetListSerializer, ExpensesByCategoriesSerializer
from quickbudget.models import Budget, Expense, Category


class ListBudgets(generics.ListCreateAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetListSerializer


class BudgetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer

    def perform_create(self, serializer):
        return serializer.save(members=[self.request.user])


class ListExpensesList(generics.ListAPIView):
    queryset = Expense.objects.all()
    serializer_class = BudgetExpenseListSerializer


class ExpensesByCategories(generics.ListAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpensesByCategoriesSerializer
    lookup_url_kwarg = "category_name"


class ExpenseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    lookup_url_kwarg = "expense_id"

    def perform_create(self, serializer):
        return serializer.save(members=[self.request.user])


class ListCategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer
