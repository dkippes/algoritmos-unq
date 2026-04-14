import sys

# UVA 455 - Periodic Strings
# Dado un string, encontrar su periodo minimo k.
# Un string tiene periodo k si puede formarse concatenando repeticiones de un substring de largo k.
#
# Tecnica: Z-array sobre el string.
# k es periodo si n % k == 0 y z[k] >= n - k
# (el sufijo en posicion k matchea todo lo que resta => el bloque s[0..k-1] se repite)
#
# Ejecutar: echo "1\n\nHoHoHo" | python3 455.py
# Link Juez: https://vjudge.net/problem/UVA-455

SUBMIT = False  # cambiar a True para enviar al juez


def z_array(s):
    n = len(s)
    z = [0] * n
    z[0] = n
    l, r = 0, 0
    for i in range(1, n):
        if i < r:
            z[i] = min(r - i, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > r:
            l, r = i, i + z[i]
    return z


def smallest_period(s):
    n = len(s)
    z = z_array(s)
    for k in range(1, n + 1):
        if n % k == 0 and (k == n or z[k] >= n - k):
            return k


def run(input_str):
    lines = input_str.strip().splitlines()
    idx = 0
    n = int(lines[idx]); idx += 1
    results = []
    for _ in range(n):
        # saltar lineas en blanco
        while idx < len(lines) and lines[idx].strip() == "":
            idx += 1
        s = lines[idx]; idx += 1
        results.append(str(smallest_period(s)))
    return "\n\n".join(results) + "\n"


def run_tests():
    def check(input_str, expected):
        got = run(input_str)
        if got == expected:
            print("PASS")
        else:
            print(f"FAIL\n  esperado: {repr(expected)}\n  obtenido: {repr(got)}")

    # Caso del enunciado
    check("1\n\nHoHoHo\n", "2\n")

    # Periodo es el string completo (no hay repeticion)
    check("1\n\nabc\n", "3\n")

    # Periodo 3
    check("1\n\nabcabcabc\n", "3\n")

    # Periodo 1 (todos iguales)
    check("1\n\naaaa\n", "1\n")

    # Multiples casos
    check("3\n\nHoHoHo\n\nabc\n\nabcabc\n", "2\n\n3\n\n3\n")


if __name__ == "__main__":
    if not SUBMIT:
        run_tests()
    else:
        data = sys.stdin.read()
        print(run(data), end="")
