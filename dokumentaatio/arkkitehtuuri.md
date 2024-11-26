# Arkkitehtuurikuvaus

## Ohjelman alustava rakenne

```mermaid
  classDiagram
    UI  ..> BudgetService
    BudgetService ..> UserRepository
    BudgetService "1" -- "*" User
    User "1" -- "*" Budget
    UserRepository ..> User
    BudgetRepository ..> Budget
```