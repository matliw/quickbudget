from rest_framework import generics, status, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from quickbudget.api.permissions import (
    BudgetMembersOnly,
    AllBudgetExpenseMembersOnly,
    ExpenseBudgetMembersOnly, IsPostOrIsAuthenticated,
    IsBudgetOwnerOrSafeMethods,
)
from quickbudget.api.serializers import (
    ExpenseSerializer,
    CategoriesSerializer,
    BudgetSerializer,
    MemberAddSerializer,
    RemoveBudgetMembersSerializer,
    UserSerializer,
)
from quickbudget.models import Budget, Expense, Category, User


class ListAddBudgets(generics.ListCreateAPIView):
    serializer_class = BudgetSerializer
    ordering = ["-last_interaction"]

    def get_queryset(self):
        return Budget.objects.filter(members=self.request.user)

    def perform_create(self, serializer):
        # Set the creator field to the current authenticated user
        serializer.validated_data['created_by'] = self.request.user

        if not serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

        # Create the budget object
        budget = serializer.save()

        # Add the current user as a member of the budget
        budget.members.add(self.request.user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class BudgetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
    lookup_url_kwarg = "budget_id"
    permission_classes = [IsBudgetOwnerOrSafeMethods]


class AddExpenses(generics.CreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [AllBudgetExpenseMembersOnly]


class ListAddExpenses(generics.ListCreateAPIView):
    serializer_class = ExpenseSerializer
    permission_classes = [AllBudgetExpenseMembersOnly]
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ["name", "total", "created_timestamp", "category"]
    ordering = ["-created_timestamp"]

    def perform_create(self, serializer):
        # Set the created_by field to the current authenticated user
        serializer.validated_data['created_by'] = self.request.user

        if not serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

        # Create the budget object
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_queryset(self):
        budget = self.kwargs["budget_id"]
        queryset = Expense.objects.filter(budget_id=budget)

        return queryset


class ExpenseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    lookup_url_kwarg = "expense_id"

    permission_classes = [ExpenseBudgetMembersOnly]


class ListCategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer


class BudgetMembers(APIView):
    permission_classes = [BudgetMembersOnly,]

    def get_queryset(self):
        return Budget.objects.filter(creator=self.request.user)

    def put(self, request, budget_id, format=None):
        budget = get_object_or_404(Budget.objects, id=budget_id)
        serializer = MemberAddSerializer(budget, data=request.data)

        if self.request.user.id != budget.creator_id:
            return Response(status=status.HTTP_403_FORBIDDEN)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, budget_id, format=None):
        budget = self.get_object(budget_id)
        serializer = RemoveBudgetMembersSerializer(budget, data=request.data)

        """1. Creator can only remove other users (non-creator member)
           2. Creator can remove himself
           3. Creator should be able to access without being a member"""

        if budget.creator_id in self.request.data['members']:
            return Response(status=status.HTTP_403_FORBIDDEN)  # prevent creator from removing himself from the member table

        if not serializer.is_valid():
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data)


class QuickbudgetUsers(APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsPostOrIsAuthenticated]

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, format=None):
        user = request.user
        user.delete()

        return Response("bye bye", status=status.HTTP_204_NO_CONTENT)


class SearchBudgetExpenses(generics.ListAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

    filter_backends = (filters.SearchFilter,)
    search_fields = ["name"]

    def get_queryset(self):
        all_user_budgets = Budget.objects.filter(members=self.request.user)
        queryset = Expense.objects.filter(budget_id__in=all_user_budgets)

        return queryset
