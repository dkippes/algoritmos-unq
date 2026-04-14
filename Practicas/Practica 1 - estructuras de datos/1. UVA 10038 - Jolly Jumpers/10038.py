import sys

# UVA 10038 - Jolly Jumpers
# Una secuencia es jolly si las diferencias absolutas entre consecutivos
# contienen todos los valores del 1 al n-1 sin faltar ninguno.
#
# Ejecutar: echo "4 1 4 2 3\n5 1 4 2 -1 6" | python3 10038.py

SUBMIT = False  # cambiar a True para enviar al juez


def is_jolly(seq):
    n = len(seq)
    if n == 1:
        return True
    seen = set()
    for i in range(1, n):
        diff = abs(seq[i] - seq[i - 1])
        seen.add(diff)
    return all(d in seen for d in range(1, n))


def run(input_str):
    output = []
    for line in input_str.strip().splitlines():
        nums = list(map(int, line.split()))
        n = nums[0]
        seq = nums[1:n + 1]
        output.append("Jolly" if is_jolly(seq) else "Not jolly")
    return "\n".join(output) + "\n"


def run_tests():
    def check(input_str, expected):
        got = run(input_str)
        if got == expected:
            print("PASS")
        else:
            print(f"FAIL\n  esperado: {repr(expected)}\n  obtenido: {repr(got)}")

    # Caso jolly del enunciado: diferencias 3,2,1 cubren 1..3
    check("4 1 4 2 3\n", "Jolly\n")

    # Caso not jolly del enunciado: diferencias 3,2,3,7 faltan 1 y 4
    check("5 1 4 2 -1 6\n", "Not jolly\n")

    # n=1: secuencia de un elemento, vacuamente jolly
    check("1 42\n", "Jolly\n")

    # n=2: una sola diferencia, siempre jolly si diff=1
    check("2 3 4\n", "Jolly\n")

    # n=2: diferencia != 1, not jolly
    check("2 1 5\n", "Not jolly\n")

    # Diferencias con negativos: 1,3,2 cubren 1..3 -> Jolly
    check("4 10 9 6 8\n", "Jolly\n")

    # Diferencia fuera de rango [1,n-1]: diff > n-1
    check("3 1 2 10\n", "Not jolly\n")

    # Multiples casos en una sola corrida
    check("4 1 4 2 3\n5 1 4 2 -1 6\n", "Jolly\nNot jolly\n")


if __name__ == "__main__":
    if not SUBMIT:
        run_tests()
    else:
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue
            nums = list(map(int, line.split()))
            n = nums[0]
            seq = nums[1:n + 1]
            print("Jolly" if is_jolly(seq) else "Not jolly")
