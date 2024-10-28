import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Configuración inicial
def initialize_grid(size, prob_tree=0.8, prob_burning=0.01):
    grid = np.zeros((size, size), dtype=int)
    for i in range(size):
        for j in range(size):
            if np.random.rand() < prob_tree:
                grid[i, j] = 1  # Árbol no quemado (Verde)
            if np.random.rand() < prob_burning:
                grid[i, j] = 2  # Árbol en llamas (Rojo)
    return grid

# Reglas del automata
def update_grid(grid, p):
    new_grid = grid.copy()
    size = grid.shape[0]
    for i in range(size):
        for j in range(size):
            if grid[i, j] == 2:  # Si el árbol está en llamas
                new_grid[i, j] = 0  # Se quema completamente (Negro)
            elif grid[i, j] == 1:  # Si el árbol no está quemado
                neighbors = [
                    grid[i2, j2]
                    for i2 in range(max(0, i - 1), min(i + 2, size))
                    for j2 in range(max(0, j - 1), min(j + 2, size))
                    if (i2 != i or j2 != j)
                ]
                if 2 in neighbors and np.random.rand() < p:
                    new_grid[i, j] = 2  # El árbol se enciende
    return new_grid

# Función para animar la simulación
def animate_forest_fire(size=50, generations=100, p=0.3):
    grid = initialize_grid(size)
    
    fig, ax = plt.subplots()
    cmap = plt.get_cmap('Greens', 3)
    mat = ax.matshow(grid, cmap=cmap)

    def update(frame):
        nonlocal grid
        grid = update_grid(grid, p)
        mat.set_data(grid)
        return [mat]

    ani = animation.FuncAnimation(fig, update, frames=generations, interval=200, repeat=False)
    plt.show()

# Ejecución de la simulación
animate_forest_fire(size=50, generations=100, p=0.3)