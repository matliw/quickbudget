from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


from quickbudget.api.permissions import (
    BudgetMembersOnly,
    AllBudgetExpenseMembersOnly,
    ExpenseBudgetMembersOnly, IsPostOrIsAuthenticated,
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
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer

    def perform_create(self, serializer):
        return serializer.save(members=[self.request.user])

    def get_queryset(self):
        return Budget.objects.filter(members=self.request.user).order_by(
            "-last_interaction"
        )


class BudgetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
    lookup_url_kwarg = "budget_id"
    permission_classes = [BudgetMembersOnly]


class AddExpenses(generics.CreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [AllBudgetExpenseMembersOnly]


class ListAddExpenses(generics.ListCreateAPIView):
    serializer_class = ExpenseSerializer
    permission_classes = [AllBudgetExpenseMembersOnly]

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
    queryset = Budget.objects.all()
    permission_classes = [BudgetMembersOnly]

    def put(self, request, budget_id, format=None):
        budget = Budget.objects.get(id=budget_id)
        serializer = MemberAddSerializer(budget, data=request.data)
        self.check_object_permissions(request, budget)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, budget_id, format=None):
        budget = Budget.objects.get(id=budget_id)
        serializer = RemoveBudgetMembersSerializer(budget, data=request.data)
        self.check_object_permissions(request, budget)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuickbudgetUsers(APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    permission_classes = [IsPostOrIsAuthenticated]

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None):
        user = request.user
        user.delete()

        return Response("bye bye", status=status.HTTP_204_NO_CONTENT)
