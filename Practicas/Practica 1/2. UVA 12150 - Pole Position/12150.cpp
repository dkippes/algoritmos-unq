#include <stdio.h>
#include <stdlib.h>

// UVA 12150 - Pole Position
// Dado el orden actual de una carrera y cuantas posiciones gano/perdio cada auto,
// reconstruir la grilla de largada. Si es imposible (colision o fuera de rango), imprimir -1.
//
// Compilar: g++ 12150.cpp -o 12150
// Ejecutar: echo "4\n1 0\n3 1\n2 -1\n4 0\n0" | ./12150

#define SUBMIT  // comentar esta linea para correr los tests en vez de la solucion

#ifndef SUBMIT
#include <sstream>
#include <string>
#include <iostream>
using namespace std;

string run(const string& input) {
    istringstream in(input);
    ostringstream out;
    int n;
    while(in >> n && n != 0) {
        int pole[1000];
        for(int i = 0; i < n; i++) pole[i] = -1;

        int valid = 1;
        for(int i = 0; i < n; i++) {
            int car, delta;
            in >> car >> delta;
            int start = i + delta;
            if(start < 0 || start >= n || pole[start] != -1) {
                valid = 0;
            } else {
                pole[start] = car;
            }
        }

        if(!valid) {
            out << -1;
        } else {
            for(int i = 0; i < n; i++) {
                if(i > 0) out << " ";
                out << pole[i];
            }
        }
        out << "\n";
    }
    return out.str();
}

#define CHECK(input, expected) do { \
    string got = run(input); \
    if(got == expected) cout << "PASS\n"; \
    else cout << "FAIL\n  esperado: " << expected << "  obtenido: " << got << "\n"; \
} while(0)

void runTests() {
    // Caso del PDF: 4 autos, resultado valido -> "1 2 3 4"
    CHECK("4\n1 0\n3 1\n2 -1\n4 0\n0\n", "1 2 3 4\n");

    // Caso imposible: dos autos mapean a la misma posicion original
    // i=0 car=1 delta=1 -> start=1; i=1 car=2 delta=0 -> start=1 -> colision
    CHECK("3\n1 1\n2 0\n3 -1\n0\n", "-1\n");

    // Caso imposible: posicion original fuera de rango
    // i=0 car=1 delta=-1 -> start=-1 -> fuera de rango
    CHECK("2\n1 -1\n2 0\n0\n", "-1\n");

    // 7 autos valido -> "5 8 2 3 7 1 9"
    // i=0 car=1 delta=5 -> start=5; i=1 car=9 delta=5 -> start=6
    // i=2 car=7 delta=2 -> start=4; i=3 car=3 delta=0 -> start=3
    // i=4 car=2 delta=-2 -> start=2; i=5 car=8 delta=-4 -> start=1
    // i=6 car=5 delta=-6 -> start=0
    CHECK("7\n1 5\n9 5\n7 2\n3 0\n2 -2\n8 -4\n5 -6\n0\n", "5 8 2 3 7 1 9\n");

    // Multiples casos de test en una sola corrida
    CHECK("4\n1 0\n3 1\n2 -1\n4 0\n2\n1 0\n2 0\n0\n", "1 2 3 4\n1 2\n");
}
#endif

int main() {
#ifndef SUBMIT
    runTests();
    return 0;
#endif

    int n;
    while(scanf("%d", &n) == 1 && n != 0) {
        int pole[1000];
        for(int i = 0; i < n; i++) pole[i] = -1;

        int valid = 1;
        for(int i = 0; i < n; i++) {
            int car, delta;
            scanf("%d %d", &car, &delta);
            int start = i + delta;
            if(start < 0 || start >= n || pole[start] != -1) {
                valid = 0;
            } else {
                pole[start] = car;
            }
        }

        if(!valid) {
            printf("-1\n");
        } else {
            for(int i = 0; i < n; i++) {
                if(i > 0) printf(" ");
                printf("%d", pole[i]);
            }
            printf("\n");
        }
    }
    return 0;
}
