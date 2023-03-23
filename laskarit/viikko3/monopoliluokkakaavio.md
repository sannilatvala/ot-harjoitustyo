```mermaid
classDiagram
	Monopoli "1" --> "2" Noppa
	Monopoli "1" --> "1" Pelilauta
	Pelilauta "1" --> "40" Ruutu
	Ruutu "1" --> "0..8" Pelinappula
	Pelinappula "1" --> "1" Pelaaja
	Pelaaja "2..8" --> "1" Monopoli
```

