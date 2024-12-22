# Testausdokumentti

Ohjelman testaus on toteutettu yksikkö- ja integraatiotesteillä `unittest` kirjastolla. Ohjelman toiminnallisuutta ja käyttöliittymää on testattu manuaalisesti kokeilemalla erilaisia odotettuja ja odottamattomia syötteitä, sekä kokeilemalla, että eri näkymät toimivat odotetusti.

## Yksikkö- ja integraatiotestaus

### Sovelluslogiikka

Sovelluslogiikan luokat `BudgetService` ja `UserService` testataan niitä vastaavilla `TestBudgetService` ja `TestUserService` testiluokilla.

### Repository-luokat

Luokat `BudgetRepository` ja `UserRepository` testataan `.env.test`-tiedostoon määritellyllä tietokannalla.

### Testauskattavuus

Testien kattavuusraportista on jätetty pois kaikki käyttöliittymään liittyvien ominaisuuksien testaus. Haarautumakattavuus muille osille on 99%

![Haarautumakattavuus](./images/coverage.png)

Testaamatta jäi `config.py`, josta jäi testaamatta pass kun kohdataan `FileNotFoundError`.

