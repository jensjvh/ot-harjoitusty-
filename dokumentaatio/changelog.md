# Changelog

## Viikko 3

### Lisäykset

* UserRepository-luokka, jolla hallitaan käyttäjätietokantaa `User`-olioiden avulla.
* Testattu UserRepositoryn perustoiminnallisuudet, eli käyttäjän luominen ja kaikkien käyttäjien poisto.
* Yksinkertainen käyttöliittymä, jossa tällä hetkellä vain kirjautumisnäkymä.
* BudgetService-luokka, johon tulee sovelluksen sovelluslogiikka.

## Viikko 4

### Lisäykset
* RegisterView ja BudgetMainView, kirjautumisnäkymä ja sovelluksen päänäkymä.
* Kirjautumisessa ja rekisteröimisessä havaitaan virheet ja ilmoitetaan käyttäjälle.
* Mahdollisuus liikkua sovelluksen näkymien välillä.
* Testejä BudgetService-luokan käyttäjätoiminnallisuuksia varten.
* Pohja Budget-oliolle.

## Viikko 5

### Lisäykset
* BudgetRepository-luokka, joka vastaa Budget-olioiden tietokantaoperaatioista.
* BudgetMainView sisältää pöydän, josta käyttäjän Budget-oliot voi nähdä.
* Käyttäjä voi luoda uusia Budget-olioita pop-up valikolla BudgetMainViewissä.
* Budget-olion alustava rakenne, joka toimii yksinkertaista tiedon tallettamista varten, sisältää budjetin määrän, kategorian ja päivämäärän.
* Testejä BudgetRepository-luokalle.

## Viikko 6

### Lisäykset
* UserService-luokka, joka vastaa käyttäjän toimintojen suorittamisesta.
* Testejä uudelle luokalle.

### Muutokset
* Refaktoroitu BudgetService luokiksi BudgetService ja UserService.

## Viikko 7

### Lisäykset

### Muutokset
* Muutettu salasanat tietokannassa Argon2-hash salasanoiksi.