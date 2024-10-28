import random
from soluciones import move_table, calculate_free_space, plot_tables

# Inicializamos las mesas
tables = [
    {"type": "redonda", "x": random.uniform(0, 5 - 1), "y": random.uniform(0, 3 - 1)} for _ in range(5)
] + [
    {"type": "cuadrada", "x": random.uniform(0, 5 - 1), "y": random.uniform(0, 3 - 1)} for _ in range(5)
]

# Función Tabu Search
def tabu_search(tables, iterations=1000, tabu_size=10):
    current_solution = tables
    current_score = calculate_free_space(current_solution)
    best_solution = current_solution
    best_score = current_score

    tabu_list = []

    for _ in range(iterations):
        new_solution = [table.copy() for table in current_solution]
        table_to_move = random.choice(new_solution)
        if move_table(new_solution, table_to_move) and new_solution not in tabu_list:
            new_score = calculate_free_space(new_solution)

            if new_score > current_score:
                current_solution = new_solution
                current_score = new_score
                tabu_list.append(new_solution)
                if len(tabu_list) > tabu_size:
                    tabu_list.pop(0)

            if current_score > best_score:
                best_solution = current_solution
                best_score = current_score

    return best_solution, best
