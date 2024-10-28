import random
from soluciones import move_table, calculate_free_space, plot_tables

# Inicializamos las mesas
tables = [
    {"type": "redonda", "x": random.uniform(0, 5 - 1), "y": random.uniform(0, 3 - 1)} for _ in range(5)
] + [
    {"type": "cuadrada", "x": random.uniform(0, 5 - 1), "y": random.uniform(0, 3 - 1)} for _ in range(5)
]

# Función Hill Climbing
def hill_climbing(tables, iterations=1000):
    current_solution = tables
    current_score = calculate_free_space(current_solution)

    for _ in range(iterations):
        new_solution = [table.copy() for table in current_solution]
        table_to_move = random.choice(new_solution)
        if move_table(new_solution, table_to_move):
            new_score = calculate_free_space(new_solution)
            if new_score > current_score:
                current_solution = new_solution
                current_score = new_score

    return current_solution, current_score

# Ejecutamos el algoritmo
solution, score = hill_climbing(tables)
plot_tables(solution, title="Hill Climbing")
