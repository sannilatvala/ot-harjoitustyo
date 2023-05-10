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

Testaamatta jäi osa GameLoop-luokasta sekä koko initialize_database.py tiedosto.

## Järjestelmätestaus

Sovellus on haettu ja sitä on testattu käyttöohjeen mukaisesti.