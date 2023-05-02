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

Peli käynnistyy aloitusnäkymään.
Pelin voi alottaa kun on asettanut itselleen käyttäjänimen ja painamalla start nappia.

### Pelin pelaaminen

Kun on painanut start nappia ja pelinäkymä on tullut esille voi pelin pelaamisen aloittaa. Matoa ohjataan nuolinäppäimillä. Kun mato syö ruokaa se kasvaa. Jos mato osuu seinään tai itseensä peli päättyy.

### Pelin lopetus

Kun peli on päättynyt siirrytään lopetusnäkymään. Näytöllä näkyy edellisen pelin kerätyt pisteet, sekä viiden peliä pelanneen parhaat tulokset. Pelin voi joko aloittaa uudestaan painamalla new game nappia tai lopettaa painamalla end game nappia.