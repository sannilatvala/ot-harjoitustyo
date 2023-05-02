## SnakeGame

Pelin tarkoituksena on ohjata matoa ja syödä ruokaa pelialueelta.
Kun mato syö ruokaa se kasvaa pituudeltaan. Kun mato osuu seinään tai
itseensä peli päättyy.

### Dokumentaatio

- [Vaatimusmaarittely](https://github.com/sannilatvala/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](https://github.com/sannilatvala/ot-harjoitustyo/blob/main/dokumentaatio/tyoaikakirjanpito.md)
- [Changelog](https://github.com/sannilatvala/ot-harjoitustyo/blob/main/dokumentaatio/changelog.md)
- [Arkkitehtuuri](https://github.com/sannilatvala/ot-harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.md)

### Releases

- [Viikko 5](https://github.com/sannilatvala/ot-harjoitustyo/releases/tag/Viikko5)
- [Viikko 6](https://github.com/sannilatvala/ot-harjoitustyo/releases/tag/Viikko6)


### Käyttöohjeet

1. Asenna riippuvuudet komennolla:
```bash
poetry install
```
2. Käynnistä peli komennolla:
```bash
poetry run invoke start
```

### Testaus

Testit pystyy suorittamaan komennolla:
```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin pystyy generoimaan komennolla:

```bash
poetry run invoke coverage-report
```

### Pylint

Tiedoston .pylintrc määrittelemät tarkistukset pystyy suorittamaan komennolla:

```bash
poetry run invoke lint
```
