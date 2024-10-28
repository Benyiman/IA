import numpy as np
import random

# Parámetros del problema
demanda = [20, 30, 15, 25, 30]  # Demanda en cada período
costo_almacenamiento = 2  # Costo por unidad almacenada
costo_escasez = 5  # Costo por unidad en escasez
capacidad_inventario = 100  # Capacidad máxima de inventario

# Clase para el sistema de hormigas
class AntColony:
    def __init__(self, num_ants, num_iterations, alpha=1, beta=2, evaporation_rate=0.5, q=100):
        self.num_ants = num_ants
        self.num_iterations = num_iterations
        self.alpha = alpha
        self.beta = beta
        self.evaporation_rate = evaporation_rate
        self.q = q
        self.num_periods = len(demanda)
        self.pheromone_matrix = np.ones((capacidad_inventario, self.num_periods))

    # Evaluar el costo de una solución
    def evaluate_solution(self, inventory_levels):
        total_cost = 0
        stock = 0
        for t in range(self.num_periods):
            stock += inventory_levels[t] - demanda[t]
            if stock >= 0:
                total_cost += stock * costo_almacenamiento
            else:
                total_cost += abs(stock) * costo_escasez
        return total_cost

    # Generar una solución (niveles de inventario)
    def generate_solution(self):
        inventory_levels = [random.randint(0, capacidad_inventario - 1) for _ in range(self.num_periods)]
        return inventory_levels

    # Actualizar feromonas
    def update_pheromones(self, solutions):
        self.pheromone_matrix *= (1 - self.evaporation_rate)
        for inventory_levels, cost in solutions:
            for t in range(self.num_periods):
                self.pheromone_matrix[inventory_levels[t], t] += self.q / cost

    # Ejecutar el sistema de hormigas
    def run(self):
        best_solution = None
        best_cost = float('inf')

        for _ in range(self.num_iterations):
            solutions = []
            for _ in range(self.num_ants):
                solution = self.generate_solution()
                cost = self.evaluate_solution(solution)
                solutions.append((solution, cost))

                if cost < best_cost:
                    best_solution = solution
                    best_cost = cost

            self.update_pheromones(solutions)

        return best_solution, best_cost

# Ejecutar 100 generaciones de Ant System y seleccionar la mejor
global_best_solution = None
global_best_cost = float('inf')

for _ in range(100):
    ant_colony = AntColony(num_ants=10, num_iterations=100)
    best_solution, best_cost = ant_colony.run()
    if best_cost < global_best_cost:
        global_best_solution = best_solution
        global_best_cost = best_cost

print("Mejor solución después de 100 generaciones (Ant System):", global_best_solution)
print("Costo de la mejor solución (Ant System):", global_best_cost)
