
from collections import namedtuple
import pandas as pd
import json

from dataclasses import dataclass

Race = namedtuple('Race',['name','drivers','teams'])

@dataclass
class Racer:
    """Class for keeping track of an item in inventory."""
    name: str
    points: int
    cost: float

def parse_races():
    races = []

    const_cost = pd.read_csv('data/constructor_value.csv')
    driver_cost = pd.read_csv('data/driver_value.csv')

    race_names = const_cost.columns[1:]

    teams = ['Mercedes','Red Bull','McLaren', 'Ferrari', 'Aston Martin',
            'Alpine', 'AlphaTauri', 'Alfa Romeo', 'Williams','Haas']

    drivers = ['Lewis Hamilton', 'Max Verstappen', 'Valtteri Bottas', 'Sergio Perez',
                'Daniel Ricciardo', 'Charles Leclerc', 'Sebastian Vettel', 'Fernando Alonso',
                'Carlos Sainz','Lance Stroll','Lando Norris','Piere Gasly','Esteban Ocon',
                'Kimi Raikkonen','Yuki Tsunoda','Antonio Giovinazzi','Nicholas Latifi',
                'George Russell','Mick Schumacher','Nikita Mazepin']

    for i,r in enumerate(race_names[:-1]):
        race_str = r.replace('GP','').replace(' ','').strip().lower()

        # plz write clean data...

        if race_str == 'french':
            race_str = 'france'
        elif race_str == 'styrian':
            race_str = 'styria'
        elif race_str == 'austrian':
            race_str = 'austria'
        elif race_str == 'british':
            race_str = 'britain'
        elif race_str == 'dutch':
            race_str = 'netherlands'
        elif race_str == 'italian':
            race_str = 'italy'
        elif race_str == 'russian':
            race_str = 'russia'
        elif race_str == 'turkish':
            race_str = 'turkey'
        elif race_str == 'hungarian':
            race_str = 'hungary'
        elif race_str == 'belgian':
            race_str = 'belgium'


        driver_perf = pd.read_csv(f'data/{race_str}_driver_performance.csv')
        constr_perf = pd.read_csv(f'data/{race_str}_constructor_performance.csv')

        drivers_tmp = []
        for d in drivers:

            season_cost_driver = driver_cost[driver_cost['Driver Name'] == d]
            cost = season_cost_driver[r].iloc[0]
            all_points = driver_perf[driver_perf['Driver Name'] == d]
            points = all_points['Fantasy Points'].iloc[0]

            drivers_tmp.append(Racer(d,points,cost))

        constructors_tmp = []
        for t in teams:
            season_cost_team = const_cost[const_cost['Constructor Name'] == t]
            cost = season_cost_team[r].iloc[0]
            all_points = constr_perf[constr_perf['Constructor Name']==t]
            points = all_points['Fantasy Points'].iloc[0]
            
            constructors_tmp.append(Racer(t,points,cost))
            

        race = Race(r, drivers_tmp,constructors_tmp)
        races.append(race)

    return races

def save_races_as_json(races,name):

    main_obj = []

    for race in races:
        race_dict = {}

        race_dict['name'] = race.name
        drivers_list = []
        race_dict['drivers'] = drivers_list

        for d in race.drivers:
            racer_dict = {}
            racer_dict['name'] = d.name
            racer_dict['cost'] = d.cost
            racer_dict['points'] = int(d.points)
            drivers_list.append(racer_dict)

        team_list = []
        race_dict['teams'] = team_list
        for t in race.teams:
            team_dict = {}
            team_dict['name'] = t.name
            team_dict['points'] = int(t.points)
            team_dict['cost'] = t.cost
            team_list.append(team_dict)

        main_obj.append(race_dict)

    with open(name,'w') as f:
        f.write(json.dumps(main_obj,indent=3))




