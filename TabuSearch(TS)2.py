import numpy as np
import random

# Parámetros del problema
demanda = [20, 30, 15, 25, 30]
costo_almacenamiento = 2
costo_escasez = 5
capacidad_inventario = 100
max_tabu_size = 10
num_iterations = 100

# Función para evaluar el costo de una solución
def evaluate_solution(inventory_levels):
    total_cost = 0
    stock = 0
    for t in range(len(demanda)):
        stock += inventory_levels[t] - demanda[t]
        if stock >= 0:
            total_cost += stock * costo_almacenamiento
        else:
            total_cost += abs(stock) * costo_escasez
    return total_cost

# Función para generar un vecino (solución cercana)
def get_neighbor(solution):
    neighbor = solution[:]
    t = random.randint(0, len(solution) - 1)
    change = random.randint(-10, 10)
    neighbor[t] = max(0, min(capacidad_inventario, neighbor[t] + change))
    return neighbor

# Ejecutar Tabu Search
def tabu_search():
    current_solution = [random.randint(0, capacidad_inventario) for _ in range(len(demanda))]
    best_solution = current_solution[:]
    best_cost = evaluate_solution(current_solution)

    tabu_list = []
    
    for _ in range(num_iterations):
        neighbors = [get_neighbor(current_solution) for _ in range(20)]
        neighbors = [n for n in neighbors if n not in tabu_list]

        if not neighbors:
            break

        neighbors_cost = [(n, evaluate_solution(n)) for n in neighbors]
        neighbors_cost.sort(key=lambda x: x[1])
        
        current_solution, current_cost = neighbors_cost[0]

        if current_cost < best_cost:
            best_solution, best_cost = current_solution, current_cost

        tabu_list.append(current_solution)
        if len(tabu_list) > max_tabu_size:
            tabu_list.pop(0)

    return best_solution, best_cost

# Ejecutar 100 generaciones de Tabu Search y seleccionar la mejor
global_best_solution = None
global_best_cost = float('inf')

for _ in range(100):
    best_solution, best_cost = tabu_search()
    if best_cost < global_best_cost:
        global_best_solution = best_solution
        global_best_cost = best_cost

print("Mejor solución después de 100 generaciones (Tabu Search):", global_best_solution)
print("Costo de la mejor solución (Tabu Search):", global_best_cost)
