import sys

# UVA 12150 - Pole Position
# Dado el orden actual de una carrera y cuantas posiciones gano/perdio cada auto,
# reconstruir la grilla de largada. Si es imposible (colision o fuera de rango), imprimir -1.
#
# Ejecutar: echo "4\n1 0\n3 1\n2 -1\n4 0\n0" | python3 12150.py

SUBMIT = False  # cambiar a True para enviar al juez


def solve(n, cars):
    pole = [-1] * n
    valid = True
    for i, (car, delta) in enumerate(cars):
        start = i + delta
        if start < 0 or start >= n or pole[start] != -1:
            valid = False
        else:
            pole[start] = car

    if not valid:
        return "-1"
    return " ".join(map(str, pole))


def run(input_str):
    output = []
    lines = input_str.strip().splitlines()
    i = 0
    while i < len(lines):
        n = int(lines[i]); i += 1
        if n == 0:
            break
        cars = []
        for _ in range(n):
            car, delta = map(int, lines[i].split()); i += 1
            cars.append((car, delta))
        output.append(solve(n, cars))
    return "\n".join(output) + "\n"


def run_tests():
    def check(input_str, expected):
        got = run(input_str)
        if got == expected:
            print("PASS")
        else:
            print(f"FAIL\n  esperado: {repr(expected)}\n  obtenido: {repr(got)}")

    # Caso del PDF: 4 autos, resultado valido -> "1 2 3 4"
    check("4\n1 0\n3 1\n2 -1\n4 0\n0\n", "1 2 3 4\n")

    # Caso imposible: dos autos mapean a la misma posicion original
    check("3\n1 1\n2 0\n3 -1\n0\n", "-1\n")

    # Caso imposible: posicion original fuera de rango
    check("2\n1 -1\n2 0\n0\n", "-1\n")

    # 7 autos valido -> "5 8 2 3 7 1 9"
    check("7\n1 5\n9 5\n7 2\n3 0\n2 -2\n8 -4\n5 -6\n0\n", "5 8 2 3 7 1 9\n")

    # Multiples casos de test en una sola corrida
    check("4\n1 0\n3 1\n2 -1\n4 0\n2\n1 0\n2 0\n0\n", "1 2 3 4\n1 2\n")


if __name__ == "__main__":
    if not SUBMIT:
        run_tests()
    else:
        lines = sys.stdin.read().splitlines()
        i = 0
        while i < len(lines):
            n = int(lines[i]); i += 1
            if n == 0:
                break
            cars = []
            for _ in range(n):
                car, delta = map(int, lines[i].split()); i += 1
                cars.append((car, delta))
            print(solve(n, cars))
