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

![](https://github.com/sannilatvala/ot-harjoitustyo/assets/119106675/1ad6df3d-8536-4ffc-a08c-6581fc407921)

Testaamatta jäi osa GameLoop-luokasta ja osa initialize_database.py tiedostostosta.

## Järjestelmätestaus

Sovellus on haettu ja sitä on testattu käyttöohjeen mukaisesti.
