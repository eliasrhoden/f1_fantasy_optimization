
from ortools.linear_solver import pywraplp

import data_parser


def formulate_as_mip(solver, racers):
    opt_vars  = []
    cost = 0
    points = 0
    for i in range(len(racers)):
        var_name = racers[i].name
        z = solver.IntVar(0,1,var_name)
        opt_vars.append(z)
        cost += z * racers[i].cost
        points += z * racers[i].points

    return opt_vars, cost, points

def optimal_fantasy_team(drivers, teams):

    solver = pywraplp.Solver.CreateSolver('SCIP')

    z_drivers, cost_drivers, points_drivers = formulate_as_mip(solver, drivers)
    z_teams, cost_teams, points_teams = formulate_as_mip(solver, teams)

    # Pick 5 drivers
    z_drivers_sum = 0
    for zd in z_drivers:
        z_drivers_sum += zd
    solver.Add(z_drivers_sum == 5)

    # Pick one team
    z_teams_sum = 0
    for zt in z_teams:
        z_teams_sum += zt
    solver.Add(z_teams_sum == 1)

    # Stay within the budget
    solver.Add(cost_drivers + cost_teams <= 100.0)

    # Maximize points
    solver.Minimize(-points_drivers - points_teams)

    # Solve
    status = solver.Solve()

    # Print solution.
    opt_team = ''
    opt_drivers = []
    if status == pywraplp.Solver.OPTIMAL or status == pywraplp.Solver.FEASIBLE:

        for i in range(len(z_teams)):
            zt = z_teams[i]
            if zt.solution_value() == 1:

                if opt_team != '':
                    raise Exception("More than one team have been chosen!")

                opt_team = teams[i].name
                
        
        for i in range(len(z_drivers)):
            zd = z_drivers[i]
            if zd.solution_value() == 1:
                opt_drivers.append(drivers[i].name)
           
    else:
        print('failed')

    return opt_drivers, opt_team


# Optimal lineup for each individual race
def main():

    races = data_parser.parse_races()
    data_parser.save_races_as_json(races,'clean_data.json')

    for race in races:
        print(f'--- {race.name} ---')
        opt_drivers, opt_team = optimal_fantasy_team(race.drivers, race.teams)

        print(f'Team: {opt_team}')
        print('Drivers: ')
        for d in opt_drivers:
            print(d)
        print('')

# Optimial lineup for all races combined
def main2():
    races = data_parser.parse_races()

    drivers = races[0].drivers
    teams = races[0].teams
    nr_races = 1
    for r in races[1:]:
        nr_races += 1
        for i in range(len(drivers)):
            name1 = drivers[i].name
            name2 = r.drivers[i].name
            assert(name1 == name2)

            drivers[i].points += r.drivers[i].points
            drivers[i].cost += r.drivers[i].cost

        for i in range(len(teams)):
            
            teams[i].points += r.teams[i].points
            teams[i].cost += r.teams[i].cost


    for i,d in enumerate(drivers):
        d.cost /= nr_races

    for i,t in enumerate(teams):
        t.cost /= nr_races

    opt_drivers, opt_team = optimal_fantasy_team(drivers, teams)

    print(f'Team: {opt_team}')
    print('Drivers: ')
    for d in opt_drivers:
        print(d)
    print('')

# Check the optimal choice for the last 5 races
def main3():
    races = data_parser.parse_races()

    drivers = races[0].drivers
    teams = races[0].teams
    nr_races = 1

    nr_last_races = 5

    for r in races[len(races)-nr_last_races:]:
        print(r.name)
        nr_races += 1
        for i in range(len(drivers)):
            name1 = drivers[i].name
            name2 = r.drivers[i].name
            assert(name1 == name2)

            drivers[i].points += r.drivers[i].points
            drivers[i].cost += r.drivers[i].cost

        for i in range(len(teams)):
            teams[i].points += r.teams[i].points
            teams[i].cost += r.teams[i].cost

    for i,d in enumerate(drivers):
        d.cost /= nr_races

    for i,t in enumerate(teams):
        t.cost /= nr_races

    opt_drivers, opt_team = optimal_fantasy_team(drivers, teams)

    print("")
    print(f'Team: {opt_team}')
    print('Drivers: ')
    for d in opt_drivers:
        print(d)
    print('')



if __name__ == '__main__':
    main()
    print("---")
    main2()
    print("---")
    main3()
