from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from quickbudget.views import ListExpensesList, ExpenseDetail, BudgetDetail, \
    ListCategoryList, ListBudgets


urlpatterns = [
    path("api/budgets/", ListBudgets.as_view(), name="get_add_budgets"),
    path("api/budgets/", BudgetDetail.as_view(), name="get_update_remove_budget"),
    path("api/budgets/<uuid:budget_id>/expenses/", ListExpensesList.as_view(), name="list_add_budget_expenses"),
    path("api/budgets/<uuid:budget_id>/expenses/<uuid:expense_id>", ExpenseDetail.as_view(), name="get_update_remove_expense_details"),
    path("api/categories/", ListCategoryList.as_view(), name="category_list"),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

]
