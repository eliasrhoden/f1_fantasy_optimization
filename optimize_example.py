
from ortools.linear_solver import pywraplp

def main():

    # Cost for each driver
    C = [10,15,5,25,15]

    # Points scored by each driver
    P = [20,80,50,90,50]

    # Budget
    B = 35

    # Create z
    solver = pywraplp.Solver.CreateSolver('SCIP')
    zs = []
    for i in range(len(C)):
        zi = solver.IntVar(0,1,f"z_{i}")
        zs.append(zi)

    # Constraint to only pick 2 drivers
    z_sum = 0
    for zi in zs:
        z_sum += zi 
    solver.Add(z_sum == 2)

    # Constraint to stay below budget and total points
    cost = 0
    points = 0
    for i,zi in enumerate(zs):
        cost += zi * C[i]
        points += zi * P[i]

    solver.Add(cost <= B)

    solver.Maximize(points)
    status = solver.Solve()

    # Print solution.
    if status == pywraplp.Solver.OPTIMAL or status == pywraplp.Solver.FEASIBLE:
        print("Pick drivers: ")
        for zi in zs:
            value = zi.solution_value()
            if value == 1:
                print(zi)
        print(f"Total cost: {cost.solution_value()}")
        print(f"Total points: {points.solution_value()}")
    else:
        print("Failed to find a solution")

    # Brute force
    bf_points = 0
    best_lineup = []
    for d1 in range(len(C)):
        for d2 in range(len(C)):
            if d1 == d2:
                continue
            cost = C[d1] + C[d2]
            points = P[d1] + P[d2]

            if cost <= B and points > bf_points:
                bf_points = points 
                best_lineup = (d1,d2)
    
    print(f"Brute force lineup: {best_lineup}")



if __name__ == '__main__':
    main()
