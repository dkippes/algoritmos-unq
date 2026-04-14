#include <stdio.h>
#include <stdlib.h>

// #define SUBMIT  // comentar esta linea para correr los tests en vez de la solucion

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

#ifndef SUBMIT
#include <cstring>
#include <string>
#include <sstream>
#include <iostream>
using namespace std;

string run(const string& input) {
    istringstream in(input);
    ostringstream out;
    int n;
    while(in >> n) {
        int seq[3000];
        for(int i = 0; i < n; i++) in >> seq[i];

        int seen[3000] = {0};
        for(int i = 1; i < n; i++) {
            int diff = seq[i] - seq[i-1];
            if(diff < 0) diff = -diff;
            seen[diff] = 1;
        }

        int jolly = 1;
        for(int i = 1; i < n; i++) {
            if(!seen[i]) { jolly = 0; break; }
        }

        out << (jolly ? "Jolly" : "Not jolly") << "\n";
    }
    return out.str();
}

#define CHECK(input, expected) do { \
    string got = run(input); \
    if(got == expected) cout << "PASS\n"; \
    else cout << "FAIL\n  esperado: " << expected << "  obtenido: " << got << "\n"; \
} while(0)

void runTests() {
    // Caso jolly del enunciado: diferencias 3,2,1 cubren 1..3
    CHECK("4 1 4 2 3\n", "Jolly\n");

    // Caso not jolly del enunciado: diferencias 3,2,3,7 faltan 1 y 4
    CHECK("5 1 4 2 -1 6\n", "Not jolly\n");

    // n=1: secuencia de un elemento, vacuamente jolly
    CHECK("1 42\n", "Jolly\n");

    // n=2: una sola diferencia, siempre jolly si diff=1
    CHECK("2 3 4\n", "Jolly\n");

    // n=2: diferencia != 1, not jolly
    CHECK("2 1 5\n", "Not jolly\n");

    // Diferencias con negativos: 1,3,2 cubren 1..3 -> Jolly
    CHECK("4 10 9 6 8\n", "Jolly\n");

    // Diferencia fuera de rango [1,n-1]: diff > n-1
    CHECK("3 1 2 10\n", "Not jolly\n");

    // Multiples casos en una sola corrida
    CHECK("4 1 4 2 3\n5 1 4 2 -1 6\n", "Jolly\nNot jolly\n");
}
#endif

int main() {
#ifndef SUBMIT
    runTests();
    return 0;
#endif

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
