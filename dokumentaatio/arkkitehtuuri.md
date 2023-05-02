# Arkkitehtuuri

## Rakenne

### Pakkausrakenne

```mermaid
graph LR;
    ui -.-> repositories
    repositories -.-> database
    src -.-> entites
    src -.-> ui

```
## Käyttöliittymä

Käyttöliitymä sisältää kolme eri näkymää:

- Pelin aloitusnäkymä
- Itse pelinäkymä
- Pelin lopetusnäkymä


### Luokkakaavio


```mermaid
classDiagram
    GameLoop ..> GameView
    GameLoop ..> GameOverView
    GameLoop ..> CreateScreen
    GameLoop ..> Snake
    GameLoop ..> Food
    GameLoop ..> GameOver
    StartView ..> StartButton
    StartView ..> CreateScreen
    GameView ..> CreateScreen
    GameView ..> Walls
    GameView ..> Food
    GameView ..> Snake
    GameOverView ..> EndGameButton
    GameOverView ..> NewGameButton
    GameOverView ..> CreateScreen
    EndGameButton ..> ButtonPosition
    NewGameButton ..> ButtonPosition

```


## Sekvenssikaaviot

### Pelin aloitus

```mermaid
sequenceDiagram
    actor User
    participant UI
    User ->> UI: create username
    User ->> UI: click start button
    participant HighScoreRepository
    UI ->> HighScoreRepository: create_user()
    HighScoreRepository -->> UI: user
```

### Pelin kulku


```mermaid
sequenceDiagram
    participant main
    participant GameLoop
    main ->> GameLoop: start()
    participant Food
    GameLoop ->> Food: new_food()
    participant CreateScreen
    GameLoop ->> CreateScreen: create_screen()
    participant Snake
    GameLoop ->> Snake: move_snake()
    Snake -->> GameLoop: snake_body
    participant GameOver
    GameLoop ->> GameOver: is_touching_wall()
    GameLoop ->> GameOver: is_touching_snake_body()
    GameOver -->> GameLoop: False
    participant GameView
    GameLoop ->> GameView: draw_game_screen()
    GameLoop ->> GameOver: is_touching_wall()
    GameLoop ->> GameOver: is_touching_snake_body()
    GameOver -->> GameLoop: True
    participant GameOverView
    GameLoop ->> GameOverView: draw_game_over_screen()
    GameOverView -->> GameLoop: True

```
