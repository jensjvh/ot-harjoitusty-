# Budjetointisovellus

Repositorio sisältää Helsingin yliopiston **Ohjelmistotekniikka** -kurssin harjoitustyön *Budjetointisovellus*.

Sovelluksella käyttäjät voivat pitää kirjaa menoista ja tuloista, sekä saada yhteenvetoja budjetista. Menoja ja tuloja voi asettaa eri kategorioihin, kuten ruoka, vapaa-aika, laskut.

## Ulkoiset kirjastot
* [Argon2](https://pypi.org/project/argon2-cffi/)
* [Matplotlib](https://matplotlib.org/)
* [tkcalendar](https://pypi.org/project/tkcalendar/)

## Uusin release

Uusin release [täällä](https://github.com/jensjvh/ot-harjoitustyo/releases/latest).

## Dokumentaatio

* [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)
* [Työaikakirjanpito](./dokumentaatio/tuntikirjanpito.md)
* [Changelog](./dokumentaatio/changelog.md)
* [Alustava luokkakaavio](./dokumentaatio/arkkitehtuuri.md)

## Käyttöohjeet

* Asenna tarvittavat packaget komennolla `poetry install`.
* Suorita ensin komento `poetry run invoke build` rakentaaksesi tietokannan.
* Tämän jälkeen testit voi suorittaa komennolla `poetry run invoke test`.
* Testikattavuus: `poetry run invoke coverage` ja `poetry run invoke coverage-report`
* Sovelluksen käynnistys: `poetry run invoke start`
