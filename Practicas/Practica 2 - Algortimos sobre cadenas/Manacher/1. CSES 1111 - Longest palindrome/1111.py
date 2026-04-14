import sys

# CSES 1111 - Longest Palindrome
# Dado un string, encontrar el substring palindromo mas largo.
#
# Tecnica: Manacher O(n)
# Transforma el string insertando '#' para unificar casos par/impar.
# p[i] = radio del palindrome centrado en i (en el string transformado).
#
# Ejecutar: echo "aybabtu" | python3 1111.py

SUBMIT = False  # cambiar a True para enviar al juez


def manacher(s):
    # transforma "abc" -> "#a#b#c#"
    t = "#" + "#".join(s) + "#"
    n = len(t)
    p = [0] * n
    c, r = 0, 0  # centro y borde derecho del palindrome mas a la derecha

    for i in range(n):
        if i < r:
            mirror = 2 * c - i
            p[i] = min(r - i, p[mirror])

        # intentar expandir
        while i - p[i] - 1 >= 0 and i + p[i] + 1 < n and t[i - p[i] - 1] == t[i + p[i] + 1]:
            p[i] += 1

        # actualizar centro y borde derecho
        if i + p[i] > r:
            c, r = i, i + p[i]

    return p, t


def longest_palindrome(s):
    p, t = manacher(s)
    # buscar el radio maximo
    max_r = max(p)
    center = p.index(max_r)
    # convertir centro y radio del string transformado al string original
    start = (center - max_r) // 2
    return s[start: start + max_r]


def run(input_str):
    s = input_str.strip()
    return longest_palindrome(s) + "\n"


def run_tests():
    def check(input_str, expected_len, is_palindrome=True):
        got = run(input_str).strip()
        ok_len = len(got) == expected_len
        ok_pal = got == got[::-1] if is_palindrome else True
        if ok_len and ok_pal:
            print(f"PASS ({repr(got)})")
        else:
            print(f"FAIL\n  esperado largo: {expected_len}\n  obtenido: {repr(got)}")

    # Caso del enunciado: "bab" largo 3
    check("aybabtu", 3)

    # String ya palindromo
    check("racecar", 7)

    # Un solo caracter
    check("a", 1)

    # Palindrome par: "abba"
    check("abba", 4)

    # Palindrome par en el medio
    check("xabbay", 4)

    # Todo el string es palindromo impar
    check("aba", 3)

    # Sin palindromo mas largo que 1
    check("abcd", 1)

    # Palindrome al final
    check("xyzaba", 3)


if __name__ == "__main__":
    if not SUBMIT:
        run_tests()
    else:
        s = sys.stdin.readline().strip()
        print(longest_palindrome(s))
