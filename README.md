# quickbudget

API documentation

<h3>API Resources:</h3>
<h3>Budgets:</h3>

| method      | url                                  | parameters | codes                                                                           |
|-------------|--------------------------------------|------------|---------------------------------------------------------------------------------|
| POST        | /budgets                             | user_ids   | 201 Created + location header,  401 Unauthorized                                |
| PUT         | /budgets/{budgetID}                  |            | 200 OK, 400 Invalid ID, 403 Forbidden, 404 Budget not found                     |
| PATCH       | /budgets/{budgetID}                  |            | 200 OK, 400 Invalid ID, 403 Forbidden, 404 Budget not found                     |
| DELETE      | /budgets/{budgetID}                  |            | 204 No Content                                                                  |
| GET         | /budget/{budgetID}                   |            | 200 successful operation, (400 invalid budgetID-optional), 404 budget not found |

<h3>Categories:</h3> 

| method | url         | parameters | codes                                            |
|--------|-------------|------------|--------------------------------------------------|
| GET    | /categories |            | 200 successful operation, 404 category not found |

<h3>Expenses:</h3>

| method | url                                   | parameters     | codes                                                         |
|--------|---------------------------------------|----------------|---------------------------------------------------------------|
| GET    | budgets/{budgetID}/expenses           | category, date | 200 successful operation, 404 budget not found, rate limit??? |
| POST   | budgets/{budgetID}/expenses/          |                | 201 Created + location header,  401 Unauthorized              |
| PUT    | budgets/{budgetID}/expenses/{entryID} |                | 200 OK, 403 Forbidden, 404 Budget not found                   |
| PATCH  | budgets/{budgetID}/expenses/{entryID} |                | 200 OK, 403 Forbidden, 404 Budget not found                   |
| DELETE | budgets/{budgetID}/expenses/{entryID} |                | 204 no content, 403 Forbidden, 404 Budget not found           |

<h3>Users:</h3>

| method | url            | parameters | codes                                                       |
|--------|----------------|------------|-------------------------------------------------------------|
| GET    | users/{userID} |            |                                                             |
| PUT    | users/{userID} |            | 200 OK, 400 Invalid ID, 403 Forbidden, 404 Budget not found |
| PATCH  | users/{userID} |            |                                                             |
| POST   | users/         |            | 201 Created + location header,  401 Unauthorized            |
| DELETE | users/{userID} |            |                                                             |


<h3>DB Resources:</h3>

User

| Field Name | Type    |
|------------|---------|
| id/user_id | id/uuid |
| first_name | text    |
| last_name  | text    |

Category

| Field Name     | Type    |
|----------------|---------|
| id/category_id | id/uuid |
| name           | text    |
| description    | text    |

Budget

| Field Name         | Type            |
|--------------------|-----------------|
| id/budget_id       | id/uuid         |
| name               | text            |
| limit              | numeric         |
| description        | text            |
| created_by/user_id | link to user.id |
| created_timestamp  | timestamp       |

Expense

| Field Name         | Type            |
|--------------------|-----------------|
| id/expense_id      | id/uuid         |
| name               | text            |
| price              | numeric         |
| quantity           | numeric         |
| total_amount       | int/numeric     |
| description/note   | text            |
| created_by/user_id | link to user.id |
| created_timestamp  | timestamp       |


