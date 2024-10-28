import numpy as np
import matplotlib.pyplot as plt
import random
from matplotlib.colors import ListedColormap

# Definición de estados
VACIO = 0
PIEDRA = 1
MAQUI = 2
PINO = 3
EUCALIPTO = 4
HUALLE = 5
ARBUSTOS = 6
ARDIENDO = 7
QUEMADO = 8

# Parámetros de resistencia al fuego (dureza) y tiempo de consumo
propiedades_fuego = {
    MAQUI: {'dureza': 3, 'tiempo_fuego': 6, 'color': 'purple'},
    PINO: {'dureza': 2, 'tiempo_fuego': 4, 'color': 'darkgreen'},
    EUCALIPTO: {'dureza': 1, 'tiempo_fuego': 4, 'color': 'green'},
    HUALLE: {'dureza': 8, 'tiempo_fuego': 8, 'color': 'brown'},
    ARBUSTOS: {'dureza': 1, 'tiempo_fuego': 1, 'color': 'lightgreen'},
    PIEDRA: {'dureza': 10, 'tiempo_fuego': 0, 'color': 'gray'}
}

# Probabilidad base de propagación del fuego
prob_propagacion = 0.4

# Inicialización del bosque
dim = 200
bosque = np.zeros((dim, dim))  # Iniciar todas las celdas como VACÍO
tiempo_ardiendo = np.zeros((dim, dim))  # Matriz para llevar el tiempo que lleva ardiendo cada celda
vegetacion_original = np.copy(bosque)  # Almacena el tipo de vegetación original de cada celda

# Definir porcentajes de cobertura
porcentaje_maqui = 0.05
porcentaje_pino = 0.70
porcentaje_eucalipto = 0.05
porcentaje_hualle = 0.1
porcentaje_arbustos = 0.08
porcentaje_piedra = 0.02

# Convertir porcentajes a número de celdas
num_celdas_maqui = int(dim * dim * porcentaje_maqui)
num_celdas_pino = int(dim * dim * porcentaje_pino)
num_celdas_eucalipto = int(dim * dim * porcentaje_eucalipto)
num_celdas_hualle = int(dim * dim * porcentaje_hualle)
num_celdas_arbustos = int(dim * dim * porcentaje_arbustos)
num_celdas_piedra = int(dim * dim * porcentaje_piedra)

# Función para asignar tipos de vegetación en el bosque
def asignar_vegetacion(tipo, num_celdas):
    for _ in range(num_celdas):
        while True:
            x, y = random.randint(0, dim-1), random.randint(0, dim-1)
            if bosque[x, y] == VACIO:  # Solo asignar si la celda está vacía
                bosque[x, y] = tipo
                vegetacion_original[x, y] = tipo  # Guardar el tipo de vegetación original
                break

# Asignar vegetación
asignar_vegetacion(MAQUI, num_celdas_maqui)
asignar_vegetacion(PINO, num_celdas_pino)
asignar_vegetacion(EUCALIPTO, num_celdas_eucalipto)
asignar_vegetacion(HUALLE, num_celdas_hualle)
asignar_vegetacion(ARBUSTOS, num_celdas_arbustos)
asignar_vegetacion(PIEDRA, num_celdas_piedra)

# Llenar las celdas vacías restantes con vegetación aleatoria
tipos_vegetacion = [MAQUI, PINO, EUCALIPTO, HUALLE, ARBUSTOS]
for x in range(dim):
    for y in range(dim):
        if bosque[x, y] == VACIO:  # Si la celda está vacía, asignar un tipo aleatorio
            bosque[x, y] = random.choice(tipos_vegetacion)
            vegetacion_original[x, y] = bosque[x, y]  # Guardar el tipo original

# Definir la cantidad de focos de incendio
num_focos = 5  # Cambia este valor para tener más o menos focos de incendio

# Función para iniciar múltiples focos de incendio aleatoriamente
def iniciar_focos_aleatorios(num_focos):
    focos_iniciados = 0
    while focos_iniciados < num_focos:
        # Generar una posición aleatoria dentro de los límites del bosque
        x, y = random.randint(0, dim-1), random.randint(0, dim-1)
        # Verificar que la posición no sea piedra y no esté ya ardiendo
        if bosque[x, y] != PIEDRA and bosque[x, y] != ARDIENDO:
            bosque[x, y] = ARDIENDO  # Iniciar el fuego en esta posición
            tiempo_ardiendo[x, y] = 1  # Comenzar a contar el tiempo de fuego
            focos_iniciados += 1  # Incrementar el contador de focos iniciados

# Iniciar los focos de incendio aleatorios
iniciar_focos_aleatorios(num_focos)
tiempo_ardiendo[0, 100] = 1  # Se empieza a contar el tiempo que la celda está ardiendo

# Crear un colormap personalizado
colores = [
    'white',  # VACÍO
    'gray',   # PIEDRA
    'purple', # MAQUI
    'darkgreen', # PINO
    'green',  # EUCALIPTO
    'brown',  # HUALLE
    'lightgreen', # ARBUSTOS
    'red',    # ARDIENDO
    'black'   # QUEMADO
]
cmap = ListedColormap(colores)

# Función para obtener los vecinos
def obtener_vecinos(x, y):
    vecinos = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if 0 <= x + i < dim and 0 <= y + j < dim:
                vecinos.append((x + i, y + j))
    return vecinos

# Crear el gráfico
plt.ion()  # Habilitar el modo interactivo
fig, ax = plt.subplots()

# Simulación
for t in range(300):
    nuevo_bosque = np.copy(bosque)
    nuevo_tiempo_ardiendo = np.copy(tiempo_ardiendo)
    for x in range(dim):
        for y in range(dim):
            if bosque[x, y] == ARDIENDO:
                # Aumentar el tiempo que lleva ardiendo
                nuevo_tiempo_ardiendo[x, y] += 1
                # Usar el tipo de vegetación original para obtener sus propiedades
                tipo_vegetacion_original = vegetacion_original[x, y]
                # Verificar si el tiempo de fuego ha alcanzado el límite para ese tipo de vegetación
                if nuevo_tiempo_ardiendo[x, y] >= propiedades_fuego[tipo_vegetacion_original]['tiempo_fuego']:
                    nuevo_bosque[x, y] = QUEMADO  # Cambiar a quemado cuando se alcance el tiempo
            elif bosque[x, y] in propiedades_fuego.keys():
                # Verificar si la vegetación se enciende
                vecinos = obtener_vecinos(x, y)
                for vx, vy in vecinos:
                    if bosque[vx, vy] == ARDIENDO:
                        tipo_vegetacion = bosque[x, y]
                        probabilidad_encendido = prob_propagacion / propiedades_fuego[tipo_vegetacion]['dureza']
                        if random.random() < probabilidad_encendido:
                            nuevo_bosque[x, y] = ARDIENDO
                            nuevo_tiempo_ardiendo[x, y] = 1  # Comenzar a contar el tiempo de fuego
                            break
    bosque = nuevo_bosque
    tiempo_ardiendo = nuevo_tiempo_ardiendo

    # Actualizar el gráfico
    ax.clear()
    ax.imshow(bosque, cmap=cmap, interpolation='nearest', vmin=VACIO, vmax=QUEMADO)
    ax.set_title(f'Tiempo: {t}')
    plt.pause(0.1)  # Pausa para permitir la actualización gráfica

plt.ioff()  # Deshabilitar el modo interactivo
plt.show()
