# quickbudget

API documentation

<h3>API Resources:</h3>
<h3>Budgets:</h3>

| method      | url                                  | parameters     | codes                                                                    |
|-------------|--------------------------------------|----------------|--------------------------------------------------------------------------|
| POST        | /budgets                             |                | 201 Created + location header,  401 Unauthorized                         |
| PUT         | /budgets/{budgetID}                  |                | 200 OK, 400 Invalid ID, 403 Forbidden, 404 Budget not found              |
| PATCH       | /budgets/{budgetID}                  |                | 200 OK, 400 Invalid ID, 403 Forbidden, 404 Budget not found              |
| DELETE      | /budgets/{budgetID}                  |                | 204 No Content                                                           |
| GET         | /budget/{budgetID}                   |                | 200 successful operation, 400 invalid budgetID, 404 budget not found     |

<h3>Categories:</h3> 

| method      | url                                  | parameters     | codes                                                                    |
|-------------|--------------------------------------|----------------|--------------------------------------------------------------------------|
| GET         | categories/{categoryIDs}             | categoryname   | 200 successful operation, 400 invalid categoryID, 404 category not found |
| POST        | categories/                          |                | 201 Created + location header,  401 Unauthorized                         |
| PUT         | categories/{categoryIDs}             |                | 200 OK, 400 Invalid ID, 403 Forbidden, 404 Budget not found                                                                         |
| DELETE      | categories/{categoryIDs}             |                |                                                                          |

<h3>Entries:</h3>

| method      | url                                  | parameters     | codes                                                                    |
|-------------|--------------------------------------|----------------|--------------------------------------------------------------------------|
| GET         | budgets/{budgetID}/entries/{entryID} | category, date | 200 successful operation, 400 invalid entryID, 404 Entry not found       |
| POST        | budgets/{budgetID}/entries/          |                | 201 Created + location header,  401 Unauthorized                         |
| PUT         | budgets/{budgetID}/entries/{entryID} |                | 200 OK, 400 Invalid ID, 403 Forbidden, 404 Budget not found                                                                         |
| PATCH       | budgets/{budgetID}/entries/{entryID} |                |                                                                          |
| DELETE      | budgets/{budgetID}/entries/{entryID} |                |                                                                          |

<h3>Users:</h3>

| method      | url                                  | parameters     | codes                                                                    |
|-------------|--------------------------------------|----------------|--------------------------------------------------------------------------|
| GET         | users/{userID}                       | username       |                                                                          |
| PUT         | users/{userID}                       |                | 200 OK, 400 Invalid ID, 403 Forbidden, 404 Budget not found                                                                         |
| PATCH       | users/{userID}                       |                |                                                                          |
| POST        | users/                               |                | 201 Created + location header,  401 Unauthorized                         |
| DELETE      | users/{userID}                       |                |                                                                          |


<h3>DB Resources:</h3>

User

| Field Name | Type |
| ----------- | ----------- |
| id/user_id | id/uuid |
| first_name | text |
| last_name | text |

Category

| Field Name | Type |
| ----------- | ----------- |
| id/category_id | id/uuid |
| name | text |
| description | text |

Budget

| Field Name | Type |
| ----------- | ----------- |
| id/budget_id | id/uuid |
| name | text |
| limit | numeric |
| description | text |
| created_by/user_id | link to user.id |
| created_timestamp | timestamp |

Expense

| Field Name | Type |
| ----------- | ----------- |
| id/expense_id | id/uuid |
| name | text |
| price | numeric |
| quantity | numeric |
| total_amount | int/numeric |
| description/note | text |
| created_by/user_id | link to user.id |
| created_timestamp | timestamp |


