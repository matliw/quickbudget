from rest_framework import generics
from quickbudget.api.serializers import ExpenseSerializer, BudgetExpenseListSerializer, CategorySerializer
from quickbudget.models import Budget, Expense, Category


class ListBudgetList(generics.ListCreateAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetExpenseListSerializer

    def perform_create(self, serializer):
        return serializer.save(members=[self.request.user])


class BudgetDetail(generics.ListCreateAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetExpenseListSerializer


class ListExpensesList(generics.ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer


class ExpenseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    lookup_url_kwarg = "item_pk"


class ListCategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
