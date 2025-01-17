import frp_rand_solver as frprs
import fastroute_problem as frp
import route_solution as rsol


dist_matrix =[
[0, 20, 30, 40],
[20, 0, 30, 5],
[30, 30, 0, 10],
[40, 5, 10, 0]]
frp_inst = frp.FastRouteProb(dist_matrix=dist_matrix)
# Run
print('Problème actuel:')
print(str(frp_inst))
print('Résoudre le problème...')
frp_solver = frprs.FrpRandSolver()

frp_sol = frp_solver.solve(frp_inst)
print('Solution retournée:')
print(str(frp_sol))
print(str(frp_sol.evaluate()))



