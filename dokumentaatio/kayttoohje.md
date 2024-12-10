# Käyttöohje

Lataa viimeisin release [täältä](https://github.com/jensjvh/ot-harjoitustyo/releases).

## Konfigurointi

Luo .env tiedosto juurihakemistoon, joka sisältää seuraavan rivin:

```
DATABASE_FILENAME=database.sqlite
```

Testejä varten luo myös .env.test tiedosto, tällä sisällöllä:

```
DATABASE_FILENAME=test-database.sqlite
```

## Käynnistäminen

Asenna riippuvuudet komennolla

```bash
poetry install
```

Suorita komento jolla rakennetaan tietokanta:

```bash
poetry run invoke build
```

Sovelluksen käynnistys:

```bash
poetry run invoke start
```

Testit ja kattavuuden voi suorittaa komennoilla `poetry run invoke test`, `poetry run invoke coverage` ja `poetry run invoke coverage-report`.

* Käyttäjän luomista varten siirry ensin rekisteröitymisnäkymään 'Create user' napilla.
* Rekisteröitymisen jälkeen voit kirjautua sisään tunnuksillasi päänäytössä.
* Päänäkymässä voit luoda budjetteja, sekä tarkastella niitä listassa.