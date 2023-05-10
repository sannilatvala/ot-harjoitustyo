## Käyttöohje

Lataa projektin viimeismmän releasen lähdekoodi

### Ohjelman käynnistäminen

Asenna ensin riippuvuudet komennolla

```bash
poetry install
```
Käynnistä sitten peli komennolla:

```bash
poetry run invoke start
```
### Pelin aloitus

Aloitusnäkymä:

![](https://github.com/sannilatvala/ot-harjoitustyo/assets/119106675/66541652-c981-46d7-8bd0-c9b6920f7634)

Peli käynnistyy aloitusnäkymään. Pelin voi alottaa kun on asettanut itselleen käyttäjänimen ja painamalla start nappia.

### Pelin pelaaminen

Pelinäkymä:

![](https://github.com/sannilatvala/ot-harjoitustyo/assets/119106675/bc63426a-d865-4003-931e-04ad88abf97f)

Kun on painanut start nappia ja pelinäkymä on tullut esille voi pelin pelaamisen aloittaa. Matoa ohjataan nuolinäppäimillä. Kun mato syö ruokaa se kasvaa. Jos mato osuu seinään tai itseensä peli päättyy.

### Pelin lopetus

Lopetusnäkymä:

![](https://github.com/sannilatvala/ot-harjoitustyo/assets/119106675/6204d979-155b-49a4-9636-39f06a41c375)

Kun peli on päättynyt siirrytään lopetusnäkymään. Näytöllä näkyy edellisen pelin kerätyt pisteet, sekä viiden peliä pelanneen parhaat tulokset. Pelin voi joko aloittaa uudestaan painamalla new game nappia tai lopettaa painamalla end game nappia.
