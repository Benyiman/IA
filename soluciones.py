# soluciones.py

import random
import math
import matplotlib.pyplot as plt

room_width = 5
room_height = 4
table_size = 1
min_distance = 0.2

# Función para verificar colisión entre mesas
def check_collision(table1, table2):
    dist = math.sqrt((table1["x"] - table2["x"]) ** 2 + (table1["y"] - table2["y"]) ** 2)
    if table1["type"] == "redonda" and table2["type"] == "redonda":
        return dist < (table_size + min_distance)
    elif table1["type"] == "cuadrada" and table2["type"] == "cuadrada":
        return (abs(table1["x"] - table2["x"]) < table_size + min_distance) and (abs(table1["y"] - table2["y"]) < table_size + min_distance)
    else:
        circle = table1 if table1["type"] == "redonda" else table2
        square = table2 if table1["type"] == "redonda" else table1
        circle_center_x = circle["x"] + table_size / 2
        circle_center_y = circle["y"] + table_size / 2
        square_x = square["x"]
        square_y = square["y"]
        closest_x = max(square_x, min(circle_center_x, square_x + table_size))
        closest_y = max(square_y, min(circle_center_y, square_y + table_size))
        return (circle_center_x - closest_x) ** 2 + (circle_center_y - closest_y) ** 2 < (table_size / 2 + min_distance) ** 2

# Función para mover una mesa sin colisiones
def move_table(tables, table_to_move):
    for _ in range(100):  # Intentamos 100 veces encontrar una posición válida
        new_x = random.uniform(0, room_width - table_size)
        new_y = random.uniform(0, room_height - table_size)
        table_to_move["x"], table_to_move["y"] = new_x, new_y
        if not any(check_collision(table_to_move, other) for other in tables if other != table_to_move):
            return True
    return False

# Función para calcular el espacio libre entre las mesas
def calculate_free_space(tables):
    total_free_space = 0
    for i in range(len(tables)):
        for j in range(i + 1, len(tables)):
            if not check_collision(tables[i], tables[j]):
                dist = math.sqrt((tables[i]["x"] - tables[j]["x"]) ** 2 + (tables[i]["y"] - tables[j]["y"]) ** 2)
                if dist < table_size + min_distance:
                    total_free_space += dist - (table_size + min_distance)
    return total_free_space

# Función para graficar las mesas
def plot_tables(tables, title="Disposición de Mesas"):
    fig, ax = plt.subplots()
    ax.set_xlim(0, room_width)
    ax.set_ylim(0, room_height)
    ax.set_title(title)
    
    for table in tables:
        if table["type"] == "redonda":
            circle = plt.Circle((table["x"] + table_size / 2, table["y"] + table_size / 2), table_size / 2, color='blue', fill=True)
            ax.add_artist(circle)
        elif table["type"] == "cuadrada":
            square = plt.Rectangle((table["x"], table["y"]), table_size, table_size, color='green', fill=True)
            ax.add_artist(square)
    
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(True)
    plt.show()
