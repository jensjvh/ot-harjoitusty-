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

## Kirjautuminen

Aluksi käyttäjä näkee kirjautumisnäkymän:

![kirjautumisnäkymä](./images/login.png)

Näkymästä voi joko kirjautua sisään olemassaolevilla tunnuksilla ja painamalla login-painiketta, tai siirtyä rekisteröitymisnäkymään Create account -painikkeella.

## Rekisteröityminen

![rekisteröitymisnäkymä](./images/register.png)

Rekisteröitymisnäkymässä voi luoda uuden käyttäjätilin uniikilla käyttäjänimellä ja vähintään kahdeksan merkkiä sisältävällä salasanalla. Käyttäjän salasana tallennetaan tietokantaan hajautettuna Argon2 -kirjastolla. Mikäli käyttäjänimi on käytössä tai salasana on liian lyhyt, ilmoittaa näkymä tästä virheviestillä.

Painamalla Create account -painiketta validilla syötteellä, käyttäjätili luodaan ja käyttäjä siirretään takaisin kirjautumisnäkymään. Painamalla Back -painiketta, voi siirtyä manuaalisesti takaisin kirjautumisnäkymään.
