from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from quickbudget.serializers import BudgetSerializer, CategorySerializer, BudgetUserSerializer, ExpenseSerializer, UserRoleSerializer
from quickbudget.models import Budget, Category, BudgetUsers, Expense, UserRole


@csrf_exempt  # exempt from cross-site security
def user_list(request):
    """
    List all code budgets, or create a new budget.
    """
    if request.method == 'GET':
        budgets = BudgetUsers.objects.all()
        serializer = BudgetUserSerializer(budgets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BudgetUserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def user_detail(request, pk):
    """
    Retrieve, update or delete a budget.
    """
    try:
        budget_user = BudgetUsers.objects.get(pk=pk)
    except BudgetUsers.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = BudgetUserSerializer(budget_user)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = BudgetUserSerializer(budget_user, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        budget_user.delete()
        return HttpResponse(status=204)