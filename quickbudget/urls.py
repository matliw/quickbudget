from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework_simplejwt.views import TokenObtainPairView, \
    TokenRefreshView

from quickbudget.views import ExpenseDetail, BudgetDetail, \
    ListCategoryList, ListAddBudgets, ListAddExpenses, BudgetMembers, \
    QuickbudgetUsers

urlpatterns = [
    path("/api/api-auth/", include("rest_framework.urls", namespace="rest-framework")),
    path("api/token/", TokenObtainPairView.as_view(), name="token-obtain_pair"),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("api/budgets/", ListAddBudgets.as_view(), name="get-add-budgets"),
    path("api/budgets/<uuid:budget_id>/", BudgetDetail.as_view(), name="get-update-remove-budget"),
    path("api/budgets/<uuid:budget_id>/members/", BudgetMembers.as_view(), name="budget-add-and-remove-members"),  # request body format: {"members": ["<user id number>", "<another user id number>"]}
    path("api/budgets/<uuid:budget_id>/expenses/", ListAddExpenses.as_view(), name="list-add-budget-expenses"),
    path("api/budgets/<uuid:budget_id>/expenses/<uuid:expense_id>/", ExpenseDetail.as_view(), name="get-update-remove-expense-details"),
    path("api/categories/", ListCategoryList.as_view(), name="category-list"),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),  # yaml schema is generated
    path("api/docs/swagger-ui/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),  # swagger-ui endpoint for API visualization
    path("api/users/", QuickbudgetUsers.as_view(), name="application-user-add-remove-members")
]


"""add roles, custom user model"""