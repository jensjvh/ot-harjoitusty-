# Vaatimusmäärittely

## Sovelluksen tarkoitus

Käyttäjät voivat luoda sovellukseen oman käyttäjätilin. Sovelluksen avulla käyttäjä voi syöttää ja kategorisoida menoja ja tuloja. Ohjelman päänäkymässä käyttäjä voi luoda uusia budjetteja, tarkastella listaa budjeteistaan, sekä tilastoja menoista ja tuloistaan. Ohjelman lisätietonäkymässä käyttäjä näkee tarkempia tietoja tuloista ja menoista. Sovelluksella voi olla samaan aikaan useampi käyttäjä. Jokaisella käyttäjällä on pääsy vain omiin tietoihinsa.

## Toiminnallisuudet

### Ennen kirjautumista

- Käyttäjä voi luoda järjestelmään käyttäjätunnuksen salasanalla
  - Tunnusten ja salasanan täytyy täyttää vaatimukset (uniikki käyttäjä, tarpeeksi pitkä)
- Käyttäjä voi kirjautua järjestelmään
- Käyttäjä voi kirjautua ulos järjestelmästä, ja sovellus estää pääsyn ilman kirjautumista.

### Kirjautumisen jälkeen

- Käyttäjä voi syöttää tulot ja menot kategorioittain.
  - Käyttäjä voi kirjata tulo- tai menotägin (esim. asuminen, ruoka, vapaa-aika).
  - Käyttäjien syöttämät tiedot lisätään tietokantaan, ja niihin pääsee käsiksi vain käyttäjä.
- Käyttäjä näkee listalta lisäämänsä budjetit.
- Käyttäjä voi poistaa listalta valittuja budjetteja.
- Käyttäjä voi tarkastella tilastoja säästöistään.
- Käyttäjä näkee kuvaajasta tulot ja menot eri päiville.

### Jatkokehitys

- Export ja Import toiminto CSV -tiedostoille.
- Haku- ja filtteröintitoiminto budjeteille.
- Käyttäjä voi muokata annettuja tietoja.
- Kalenterinäkymä.
- Käyttäjätunnuksen ja tietojen poisto.
- Ennuste käyttäjän budjetin kehityksestä.
