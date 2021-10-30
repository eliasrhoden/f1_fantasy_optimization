# F1 Fantasy optimization

Rewriting the choice of F1 Fantasy team lineup as a mixed integer program. Solved using Google OR-tools.
https://developers.google.com/optimization


It's worth mentioning that the results have not been verified other than *by eye*, and for next year's season, the goal is to include Turbo and Mega drivers in the optimization problem (And also the nr of substitutions allowed).

## Data
The data is obtained from: https://www.kaggle.com/prathamsharma123/formula-1-fantasy-2021

Where the driver/team cost for each GP is listed and also the point change after each GP.

There are some incosistency in the data, mainley the names don't allways match for all files, so I've also saved the cleaned data as a JSON (`clean_data.json`).


## Optimal lineups

I've optimized 3 different cases:
* one lineup for each GP
* One lineup for the whole season
* One lineup for the last 5 races

### Optimal lineup for each GP
```
--- Bahrain GP ---
Team: Red Bull
Drivers: 
Max Verstappen
Valtteri Bottas
Lando Norris
George Russell
Mick Schumacher

--- Imola GP ---
Team: McLaren
Drivers: 
Max Verstappen
Charles Leclerc
Carlos Sainz
Lando Norris
Kimi Raikkonen

--- Portugal GP ---
Team: Red Bull
Drivers: 
Max Verstappen
Sergio Perez
Lando Norris
Esteban Ocon
Mick Schumacher

--- Spain GP ---
Team: Red Bull
Drivers: 
Max Verstappen
Daniel Ricciardo
Charles Leclerc
Nicholas Latifi
George Russell

--- Monaco GP ---
Team: Red Bull
Drivers: 
Max Verstappen
Sebastian Vettel
Carlos Sainz
Lando Norris
Nikita Mazepin

--- Azerbaijan GP ---
Team: Red Bull
Drivers: 
Sergio Perez
Sebastian Vettel
Fernando Alonso
Lando Norris
Piere Gasly

--- French GP ---
Team: Red Bull
Drivers: 
Max Verstappen
Sergio Perez
Lando Norris
Antonio Giovinazzi
George Russell

--- Styrian GP ---
Team: Red Bull
Drivers: 
Max Verstappen
Valtteri Bottas
Kimi Raikkonen
Yuki Tsunoda
Mick Schumacher

--- Austrian GP ---
Team: Red Bull
Drivers: 
Max Verstappen
Carlos Sainz
Lando Norris
Piere Gasly
Mick Schumacher

--- British GP ---
Team: Ferrari
Drivers: 
Lewis Hamilton
Charles Leclerc
Lando Norris
Yuki Tsunoda
George Russell

--- Hungarian GP ---
Team: Alpine
Drivers: 
Lewis Hamilton
Fernando Alonso
Carlos Sainz
Piere Gasly
Esteban Ocon

--- Belgian GP ---
Team: Williams
Drivers: 
Lewis Hamilton
Max Verstappen
Daniel Ricciardo
Piere Gasly
George Russell

--- Dutch GP ---
Team: Red Bull
Drivers: 
Max Verstappen
Fernando Alonso
Lando Norris
Piere Gasly
Nicholas Latifi

--- Italian GP ---
Team: McLaren
Drivers: 
Valtteri Bottas
Daniel Ricciardo
Charles Leclerc
Lando Norris
George Russell

--- Russian GP ---
Team: Mercedes
Drivers: 
Daniel Ricciardo
Fernando Alonso
Carlos Sainz
Kimi Raikkonen
George Russell

--- Turkish GP ---
Team: Red Bull
Drivers: 
Valtteri Bottas
Sergio Perez
Charles Leclerc
Antonio Giovinazzi
George Russell

--- USA GP ---
Team: Red Bull
Drivers: 
Max Verstappen
Sergio Perez
Charles Leclerc
George Russell
Mick Schumacher
```

### Optimal lineup for the whole season
```
Team: Red Bull
Drivers: 
Max Verstappen
Carlos Sainz
Lando Norris
Piere Gasly
George Russell
```

### Optimal lineup for the last 5 races
As of writing this, the last GP was in the US. 
```
Dutch GP
Italian GP
Russian GP
Turkish GP
USA GP

Team: Red Bull
Drivers: 
Valtteri Bottas
Daniel Ricciardo
Carlos Sainz
Lando Norris
Mick Schumacher
```

