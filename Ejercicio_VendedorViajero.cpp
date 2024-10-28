#include <iostream>
#include <cstdlib>  // Para rand() y srand()
#include <ctime>    // Para time()

int aleat() {
    return (rand() % 100) + 1;
}

int main() {
    const int N = 4;
    int peso[N][N];
    srand(time(0));  // Inicializar la semilla para los números aleatorios

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            peso[i][j] = -1;  // Inicializa con -1
            if (i == j) {
                peso[i][j] = 0;  // Los elementos en la diagonal son 0
            } else if (peso[i][j] == -1) {
                int num_aleat = aleat();
                peso[i][j] = num_aleat;
                peso[j][i] = num_aleat;  // Mantener la simetría
            }
        }
    }

    // Mostrar la matriz
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            std::cout << peso[i][j] << "\t";
        }
        std::cout << std::endl;
    }

    return 0;
}
