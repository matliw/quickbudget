from django.urls import path

from quickbudget.views import ListExpensesList, ExpenseDetail, BudgetDetail, \
    ListCategoryList, ListBudgets, ExpensesByCategories, CreateExpense

urlpatterns = [
    path("api/budgets/", ListBudgets.as_view(), name="all_budgets"),
    path("api/budgets/", BudgetDetail.as_view(), name="add_budget"),
    path("api/budgets/<uuid:budget_id>/", BudgetDetail.as_view(), name="budget_detail"),
    path("api/budgets/<uuid:budget_id>/expenses/", ListExpensesList.as_view(), name="list_budget_expenses"),
    path("api/budgets/<uuid:budget_id>/expenses/", CreateExpense.as_view(), name="list_budget_expenses"),
    path("api/budgets/<uuid:budget_id>/expenses/<str:category_name>/", ExpensesByCategories.as_view(), name="expenses_by_category"),
    path("api/budgets/<uuid:budget_id>/expenses/<uuid:expense_id>", ExpenseDetail.as_view(), name="expense_details"),
    path("api/categories/", ListCategoryList.as_view(), name="category_list"),
]
