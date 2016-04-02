import numpy as np
from BasicFunctions import getRateL1O, flip

# Búsqueda Tabú
def tabuSearch(train_data, train_categ):
    num_features = len(train_data[0])
    max_neighbours = 30

    # Partimos de un vector solución aleatorio
    solution = np.random.random(size=num_features)<0.5
    cost_current_sol = getRateL1O(train_data[:,solution],train_categ)

    # Mejor solución encontrada
    best_solution = np.copy(solution)
    cost_best_sol = cost_current_sol

    # Determinamos el número de iteraciones
    max_iter = 15000/max_neighbours

    # Lista tabú
    tabu_list = np.array([-1 for i in range(num_features/3)])
    tabu_index = 0
    choosen = False

    for i in range(max_iter):
        neighbors = np.random.random_integers(0, num_features-1, max_neighbours)
        rates = np.array([[j,0] for j in neighbors], object)
        for j in range(max_neighbours):
            flip(solution, neighbors[j])
            rates[j, 1] = getRateL1O(training_data[:,solution],train_categ)
            flip(solution, neighbors[j])

        rates[rates[:,1].argsort()]

        for j in range(max_neighbours):
            if rates[j,1] > cost_best_sol:
                cost_best_sol =  rates[j,1]
                choosen = True
            elif rates[j,0] not in tabu_list:
                choosen = True
            else:
                choosen = False

            if(choosen):
                flip(solution, rates[j,0])
                tabu_list[tabu_index] = rates[j,0]
                tabu_index = (tabu_index+1)%len(tabu_list)


    return solution
