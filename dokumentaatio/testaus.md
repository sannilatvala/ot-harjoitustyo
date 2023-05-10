# Testausdokumentti

Ohjelman yksikkö- ja integraatiotestaus on tehty automatisoidusti unittestilla ja järjestelmätestit on tehty manuaalisesti.

## Yksikkö- ja integraatiotestaus

### Sovelluslogiikka

Pelin sovelluslogiikasta vastaavat luokat testataan viidellä eri testiluokalla:
- TestFood
- TestGameLoop
- TestGameOver
- TestSnake
- TestWalls

### Repositorio-luokat

HighScoreRepository-luokka testataan TestHighScoreRepository-luokalla

### Testikattavuus

![](https://github.com/sannilatvala/ot-harjoitustyo/assets/119106675/30fb0545-54cd-4399-bd9d-6a3c867f200e)

Testaamatta jäi osa GameLoop-luokasta sekä koko initialize_database.py tiedosto.

## Järjestelmätestaus

Sovellus on haettu ja sitä on testattu käyttöohjeen mukaisesti.
