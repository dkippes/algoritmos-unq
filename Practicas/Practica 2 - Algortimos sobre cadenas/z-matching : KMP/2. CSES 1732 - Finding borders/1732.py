import sys

# CSES 1732 - Finding Borders
# Dado un string, encontrar todas las longitudes de sus borders.
# Un border es un prefijo que tambien es sufijo, pero no el string completo.
#
# Tecnica: Z-array sobre el string.
# z[i] == n - i significa que el sufijo que empieza en i matchea un prefijo de largo n-i,
# o sea que hay un border de longitud n-i.
#
# Ejecutar: echo "abcababcab" | python3 1732.py
# Link Juez: https://cses.fi/problemset/task/1732

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


def find_borders(s):
    n = len(s)
    z = z_array(s)
    borders = []
    for i in range(1, n):
        if z[i] == n - i:
            borders.append(n - i)
    borders.sort()
    return borders


def run(input_str):
    s = input_str.strip()
    result = find_borders(s)
    return " ".join(map(str, result)) + "\n"


def run_tests():
    def check(input_str, expected):
        got = run(input_str)
        if got == expected:
            print("PASS")
        else:
            print(f"FAIL\n  esperado: {repr(expected)}\n  obtenido: {repr(got)}")

    # Caso del enunciado
    check("abcababcab\n", "2 5\n")

    # Sin borders
    check("abcdef\n", "\n")

    # Todos iguales: todos los prefijos son borders
    check("aaaa\n", "1 2 3\n")

    # Un solo border
    check("abab\n", "2\n")

    # String de un caracter: no hay borders
    check("a\n", "\n")

    # Dos caracteres iguales
    check("aa\n", "1\n")


if __name__ == "__main__":
    if not SUBMIT:
        run_tests()
    else:
        s = sys.stdin.readline().strip()
        result = find_borders(s)
        print(*result)
