import sys

# CSES 1753 - String Matching
# Dado un string y un patron, contar cuantas veces aparece el patron en el string.
#
# Tecnica: Z-array sobre "patron + $ + texto"
# Z[i] >= len(patron) significa que el patron aparece en esa posicion del texto.
#
# Ejecutar: echo "saippuakauppias\npp" | python3 1753.py
# Link Juez: https://vjudge.net/problem/CSES-1753

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


def count_occurrences(text, pattern):
    if len(pattern) > len(text):
        return 0
    combined = pattern + "$" + text
    z = z_array(combined)
    m = len(pattern)
    # las posiciones del texto empiezan en m+1 dentro de combined
    return sum(1 for i in range(m + 1, len(combined)) if z[i] >= m)


def run(input_str):
    lines = input_str.strip().splitlines()
    text = lines[0]
    pattern = lines[1]
    return str(count_occurrences(text, pattern)) + "\n"


def run_tests():
    def check(input_str, expected):
        got = run(input_str)
        if got == expected:
            print("PASS")
        else:
            print(f"FAIL\n  esperado: {repr(expected)}\n  obtenido: {repr(got)}")

    # Caso del enunciado: "pp" aparece 2 veces en "saippuakauppias"
    check("saippuakauppias\npp\n", "2\n")

    # Patron no aparece
    check("abcdef\nxyz\n", "0\n")

    # Patron igual al texto
    check("abc\nabc\n", "1\n")

    # Patron mas largo que el texto
    check("ab\nabc\n", "0\n")

    # Patron de un caracter
    check("aaaa\na\n", "4\n")

    # Ocurrencias solapadas
    check("aaaa\naa\n", "3\n")

    # Una sola ocurrencia al principio
    check("abcdef\nabc\n", "1\n")

    # Una sola ocurrencia al final
    check("xyzabc\nabc\n", "1\n")


if __name__ == "__main__":
    if not SUBMIT:
        run_tests()
    else:
        data = sys.stdin.read().splitlines()
        text = data[0]
        pattern = data[1]
        print(count_occurrences(text, pattern))


## EJEMPLO DE COMO MANDARLO AL JUEZ
# import sys

# def z_array(s):
#    n = len(s)
#    z = [0] * n
#    z[0] = n
#    l, r = 0, 0
#    for i in range(1, n):
#        if i < r:
#            z[i] = min(r - i, z[i - l])
#        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
#            z[i] += 1
#        if i + z[i] > r:
#            l, r = i, i + z[i]
#    return z


# def count_occurrences(text, pattern):
#    if len(pattern) > len(text):
#        return 0
#    combined = pattern + "$" + text
#    z = z_array(combined)
#    m = len(pattern)
#    # las posiciones del texto empiezan en m+1 dentro de combined
#    return sum(1 for i in range(m + 1, len(combined)) if z[i] >= m)


# def run(input_str):
#    lines = input_str.strip().splitlines()
#    text = lines[0]
#    pattern = lines[1]
#    return str(count_occurrences(text, pattern)) + "\n"

# if __name__ == "__main__":
#        data = sys.stdin.read().splitlines()
#        text = data[0]
#        pattern = data[1]
#        print(count_occurrences(text, pattern))
