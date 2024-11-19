# Budjetointisovellus

Repositorio sisältää Helsingin yliopiston **Ohjelmistotekniikka** -kurssin harjoitustyön *Budjetointisovellus*.

Sovelluksella käyttäjät voivat pitää kirjaa menoista ja tuloista, sekä saada yhteenvetoja budjetista. Menoja ja tuloja voi asettaa eri kategorioihin, kuten ruoka, vapaa-aika, laskut.

## Dokumentaatio

* [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)
* [Työaikakirjanpito](./dokumentaatio/tuntikirjanpito.md)
* [Changelog](./dokumentaatio/changelog.md)

## Käyttöohjeet

* Suorita ensin komento `poetry run invoke build` rakentaaksesi tietokannan.
* Tämän jälkeen testit voi suorittaa komennolla `poetry run invoke test`.
* Testikattavuus: `poetry run invoke coverage` ja `poetry run invoke coverage-report`