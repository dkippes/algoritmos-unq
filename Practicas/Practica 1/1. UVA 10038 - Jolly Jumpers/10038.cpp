#include <stdio.h>
#include <stdlib.h>

// UVA 10038 - Jolly Jumpers
// Una secuencia es jolly si las diferencias absolutas entre consecutivos
// contienen todos los valores del 1 al n-1 sin faltar ninguno.
//
// Compilar: g++ 10038.cpp -o 10038
// Ejecutar: echo "4 1 4 2 3\n5 1 4 2 -1 6" | ./10038
//
// Ejemplo:
//   Input:  4 1 4 2 3   -> diferencias: 3,2,1 -> cubre 1..3 -> Jolly
//   Input:  5 1 4 2 -1 6 -> diferencias: 3,2,3,7 -> falta 1 y 4 -> Not jolly

int main() {
    int n;
    // cada iteracion procesa un caso: lee n, luego los n numeros de la secuencia
    while (scanf("%d", &n) == 1) {
        int seq[3000];
        for (int i = 0; i < n; i++) {
            scanf("%d", &seq[i]);
        }

        // seen[d] = 1 si la diferencia d aparecio entre elementos consecutivos
        int seen[3000] = {0};
        for (int i = 1; i < n; i++) {
            int diff = seq[i] - seq[i-1];
            if (diff < 0) diff = -diff;  // valor absoluto
            seen[diff] = 1;
        }

        // verificar que aparecieron todas las diferencias del 1 al n-1
        int jolly = 1;
        for (int i = 1; i < n; i++) {
            if (!seen[i]) {
                jolly = 0;
                break;
            }
        }

        if (jolly) printf("Jolly\n");
        else printf("Not jolly\n");
    }
    return 0;
}
