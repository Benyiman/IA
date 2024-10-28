import random
import math
from soluciones import move_table, calculate_free_space, plot_tables

# Inicializamos las mesas
tables = [
    {"type": "redonda", "x": random.uniform(0, 5 - 1), "y": random.uniform(0, 3 - 1)} for _ in range(5)
] + [
    {"type": "cuadrada", "x": random.uniform(0, 5 - 1), "y": random.uniform(0, 3 - 1)} for _ in range(5)
]

# Función de Simulated Annealing
def simulated_annealing(tables, iterations=1000, temp=1000, cooling_rate=0.995):
    current_solution = tables
    current_score = calculate_free_space(current_solution)
    best_solution = current_solution
    best_score = current_score

    for _ in range(iterations):
        new_solution = [table.copy() for table in current_solution]
        table_to_move = random.choice(new_solution)
        if move_table(new_solution, table_to_move):
            new_score = calculate_free_space(new_solution)
            delta = new_score - current_score

            if delta > 0 or random.uniform(0, 1) < math.exp(delta / temp):
                current_solution = new_solution
                current_score = new_score

            if current_score > best_score:
                best_solution = current_solution
                best_score = current_score

            temp *= cooling_rate

    return best_solution, best_score

# Ejecutamos el algoritmo
solution, score = simulated_annealing(tables)
plot_tables(solution, title="Simulated Annealing")
