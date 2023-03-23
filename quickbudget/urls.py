from django.urls import path

from quickbudget.views import ListExpensesList, ExpenseDetail, BudgetDetail, ListBudgetList, ListCategoryList


urlpatterns = [
    path("api/budgets/", ListBudgetList.as_view(), name="all_budgets"),
    path("api/budgets/<uuid:pk>/", BudgetDetail.as_view(), name="budget_detail"),
    path("api/budgets/<uuid:pk>/expenses/", ListExpensesList.as_view(), name="expense_list"),
    path("api/budgets/<uuid:pk>/expenses/<uuid:item_pk>", ExpenseDetail.as_view(), name="expense_details"),
    path("api/categories/", ListCategoryList.as_view(), name="category_list"),
    path("api/expenses/", ListExpensesList.as_view(), name="expense_list"),
    path("api/categories/<uuid:item_pk>", ExpenseDetail.as_view(), name="expense_details"),
]