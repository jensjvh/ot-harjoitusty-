# Arkkitehtuurikuvaus

## Pakkausrakenne

```mermaid
  graph LR
    UI --> Services
    Services --> Repositories
    Repositories --> Entities
    Services --> Entities
    UI --> Utils
    Services --> Utils
```

Sovelluksen rakenteessa on kerrokset `UI`, `Services`, `Repositories` ja `Entities`. `UI` kerros kommunikoi `Services` kerroksen kanssa, `Services` `Repositories` ja `Entities` kanssa, sekä `Repositories` `Entities` kanssa. Sovelluksessa on myös `Utils` kerros, jota käyttävät `UI` ja `Services` kerros.

## Tietojen tallennus

Luokat `BudgetRepository` ja `UserRepository` ovat vastuussa sovelluksen tietojen tallentamisesta. Molemmat käyttävät SQLite-tietokantaa, jonka tablet alustetaan tiedostossa [initialize_database.py](../src/initialize_database.py). Tiedostot sijaitsevat juurihakemiston `data` hakemistossa, ja tiedostojen nimet on määritelty [.env](../.env)-tiedostossa. Testauksessa tiedostojen nimet on määritelty [.env.test](../.env.test)-tiedostossa.

## Sovelluslogiikka

```mermaid
  classDiagram
    UI  ..> BudgetService
    UI  ..> UserService
    UI  ..> Utils
    BudgetService ..> UserRepository
    BudgetService ..> BudgetRepository
    BudgetService ..> Utils
    UserService ..> UserRepository
    UserService ..> Utils
    BudgetService "1" -- "*" User
    User "1" -- "*" Budget
    UserRepository ..> User
    BudgetRepository ..> Budget
```

## Käynnistys ja kirjautuminen

```mermaid
sequenceDiagram
    actor User
    participant UI
    participant UserService
    participant UserRepository
    UI->>UI: _show_login_view()
    User->>UI: Login with username and password
    UI->>UserService: login(username, password)
    UserService->>UserRepository: find_user(username)
    UserRepository->>UserService: user
    UserService->>UI: user
    UI->>UI: _show_budget_main_view()
```

Käynnistyksen yhteydessä UI kutsuu _show_login_view()-metodia, jolla näytetään kirjautumisnäkymä käyttäjälle. Käyttäjän painamalla kirjautumispainiketta, kutsuu UI `UserService` palvelun login()-metodia käyttäjätunnuksella ja salasanalla. `UserService` kutsuu `UserRepository` luokan find_user()-metodia parametrina käyttäjänimi, joka palauttaa `User` olion, jos käyttäjä löytyy. `UserService` palauttaa tämän `User` olion, ja UI ohjaa käyttäjän sovelluksen päänäkymään metodilla _show_budget_main_view().

## Rekisteröityminen

```mermaid
sequenceDiagram
    actor User
    participant UI
    participant UserService
    participant UserRepository
    participant new_user
    UI->>UI: _show_login_view()
    User->>UI: Click "Create account" button
    UI->>UI: _show_register_view()
    User->>UI: Register with username and password
    UI->>UserService: create_user(username, password)
    UserService->>UserRepository: find_user(username)
    UserRepository->>UserService: None
    UserService->>new_user: User(username, password)
    UserService->>UserRepository: create(new_user)
    UserRepository->>UserService: user
    UserService->>UI: user
    UI->>UI: _show_budget_main_view()
```

UI kutsuu _show_login_view()-metodia, joka näyttää käyttäjälle kirjautumisnäkymän. Käyttäjä painaa "Create account" -painiketta, jolloin UI kutsuu _show_register_view()-metodia, joka näyttää rekisteröitymisnäkymän. UI kutsuu `UserService`-palvelun create_user()-metodia, jossa käyttäjätunnus ja salasana annetaan parametreina. `UserService` kutsuu `UserRepository`-luokan find_user()-metodia tarkistaakseen, onko käyttäjätunnus jo olemassa. `UserRepository` ei löydä käyttäjää, joten se palauttaa None. `UserService` luo uuden käyttäjän User-olion muodossa, käyttäjätunnuksella ja salasanalla. UserService kutsuu `UserRepository`-luokkaa create()-metodilla luodakseen uuden käyttäjän tietokantaan. `UserRepository` palauttaa luodun käyttäjän UserService-palvelulle. UserService palauttaa käyttäjän UI:lle. UI ohjaa käyttäjän sovelluksen päänäkymään kutsumalla _show_budget_main_view()-metodia.

## Käyttöliittymä

Sovelluksessa on näkymät kirjautumiselle, rekisteröitymiselle, budjettien tarkastelulle, budjettien lisätiedoille, sekä pieni popup näkymä budjettien lisäykselle.

### Budjettien luominen

```mermaid
sequenceDiagram
    actor User
    participant UI
    participant BudgetService
    participant BudgetRepository
    UI->>UI: _show_budget_main_view()
    User->>UI: Create Budget
    UI->>BudgetService: create_budget(user, amount, category, date, tag)
    BudgetService->>BudgetRepository: create(budget)
    BudgetRepository->>BudgetService: budget
    BudgetService->>UI: budget
    UI->>UI: refresh_budget_list()
```

### Budjettien poistaminen

```mermaid
sequenceDiagram
    actor User
    participant UI
    participant BudgetService
    participant BudgetRepository
    UI->>UI: _show_budget_main_view()
    User->>UI: Delete Selected Budget
    UI->>BudgetService: delete_budget_by_id(budget_id)
    BudgetService->>BudgetRepository: delete_budget_by_id(budget_id)
    UI->>UI: refresh_budget_list()
```