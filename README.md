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

* [Käyttöohje](./dokumentaatio/kayttoohje.md)
* [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)
* [Arkkitehtuurikuvaus](./dokumentaatio/arkkitehtuuri.md)
* [Testausdokumentti](./dokumentaatio/testaus.md)
* [Työaikakirjanpito](./dokumentaatio/tuntikirjanpito.md)
* [Changelog](./dokumentaatio/changelog.md)

## Asennus

1. Asenna tarvittavat packaget komennolla `poetry install`.
2. Suorita ensin komento `poetry run invoke build` rakentaaksesi tietokannan.
3. Tämän jälkeen sovelluksen voi käynnistää komennolla `poetry run invoke start`.

## Testaus

* Testikattavuus: `poetry run invoke coverage` ja `poetry run invoke coverage-report`
* Testien suoritus: `poetry run invoke test`

## Muut komennot

* `poetry run invoke lint` tarkistaa tiedoston [.pylintrc](./.pylintrc) määrittelemät tarkastukset.
* `poetry run invoke format` muuttaa rekursiivisesti projektin Python-tiedostot vastaamaan PEP 8 -tyyliopasta.