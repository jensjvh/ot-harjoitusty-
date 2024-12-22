# Vaatimusmäärittely

## Sovelluksen tarkoitus

Käyttäjät voivat luoda sovellukseen oman käyttäjätilin. Sovelluksen avulla käyttäjä voi syöttää ja kategorisoida menoja ja tuloja. Ohjelman päänäkymässä käyttäjä voi luoda uusia budjetteja, tarkastella listaa budjeteistaan, sekä tilastoja menoista ja tuloistaan. Ohjelman lisätietonäkymässä käyttäjä näkee tarkempia tietoja tuloista ja menoista. Sovelluksella voi olla samaan aikaan useampi käyttäjä. Jokaisella käyttäjällä on pääsy vain omiin tietoihinsa.

## Toiminnallisuudet

### Perusversio

- [x] Yksinkertainen käyttöliittymä.
- [x] Käyttäjä voi luoda järjestelmään käyttäjätunnuksen salasanalla
  - [x] Tunnusten ja salasanan täytyy täyttää vaatimukset (uniikki käyttäjä, tarpeeksi pitkä)
- [x] Käyttäjä voi kirjautua järjestelmään
- [x] Käyttäjä voi kirjautua ulos järjestelmästä, ja sovellus estää pääsyn ilman kirjautumista.
- [x] Käyttäjä voi syöttää tulot ja menot kategorioittain.
  - [ ] Käyttäjä voi valita kustannusluokan (esim. asuminen, ruoka, vapaa-aika).
  - [x] Jokaisella käyttäjällä on oma tietorakenne tai tiedosto, jossa säilytetään käyttäjän yksilölliset tiedot.
- [x] Käyttäjä voi poistaa päänäkymästä luotuja budjetti-objekteja.
- [x] Käyttäjä voi tarkastella tulojen ja menojen välistä erotusta.
- [x] Käyttäjä näkee kuvaajasta tulot ja menot eri päiville.

### Jatkokehitys

- [ ] Export ja Import toiminto CSV -tiedostoille.
- [ ] Haku- ja filtteröintitoiminto budjeteille.
- [ ] Käyttäjä voi muokata annettuja tietoja
- [ ] Kalenterinäkymä.
- [ ] Käyttäjä voi tarkastella kuukausittaista yhteenvetoa.
  - [ ] Yhteenvedossa näytetään menot kategoriakohtaisesti.
- [ ] Käyttäjätunnuksen ja tietojen poisto.
- [ ] Ennuste käyttäjän budjetin kehityksestä.
