import sys

# SPOJ - PHONELST - Phone List
# Dada una lista de numeros de telefono, determinar si es consistente:
# ningun numero es prefijo de otro.
#
# Tecnica: Trie (prefix tree)
# Al insertar cada numero, si pasamos por un nodo marcado como fin -> colision
# Si al terminar de insertar el nodo tiene hijos -> colision
#
# Ejecutar: echo "2\n3\n911\n97625999\n91125426\n5\n113\n12340\n123440\n12345\n98346" | python3 phonelst.py

SUBMIT = False  # cambiar a True para enviar al juez


def make_node():
    return {"hijos": {}, "es_fin": False}


def is_consistent(numbers):
    raiz = make_node()

    for number in numbers:
        nodo = raiz
        for i, ch in enumerate(number):
            # si algun prefijo ya termina aca -> colision
            if nodo["es_fin"]:
                return False
            if ch not in nodo["hijos"]:
                nodo["hijos"][ch] = make_node()
            nodo = nodo["hijos"][ch]

        # si al terminar este numero el nodo tiene hijos -> otro numero lo extiende
        # o si ya estaba marcado como fin -> numero duplicado
        if nodo["hijos"] or nodo["es_fin"]:
            return False
        nodo["es_fin"] = True

    return True


def run(input_str):
    output = []
    lines = input_str.strip().splitlines()
    i = 0
    t = int(lines[i]); i += 1
    for _ in range(t):
        n = int(lines[i]); i += 1
        numbers = []
        for _ in range(n):
            numbers.append(lines[i]); i += 1
        output.append("YES" if is_consistent(numbers) else "NO")
    return "\n".join(output) + "\n"


def run_tests():
    def check(input_str, expected):
        got = run(input_str)
        if got == expected:
            print("PASS")
        else:
            print(f"FAIL\n  esperado: {repr(expected)}\n  obtenido: {repr(got)}")

    # Caso del enunciado: "911" es prefijo de "91125426" -> NO
    check("1\n3\n911\n97625999\n91125426\n", "NO\n")

    # Caso del enunciado: lista consistente -> YES
    check("1\n5\n113\n12340\n123440\n12345\n98346\n", "YES\n")

    # Dos casos juntos
    check("2\n3\n911\n97625999\n91125426\n5\n113\n12340\n123440\n12345\n98346\n", "NO\nYES\n")

    # Un solo numero -> siempre consistente
    check("1\n1\n911\n", "YES\n")

    # Numero identico a otro -> es prefijo de si mismo
    check("1\n2\n123\n123\n", "NO\n")

    # Prefijo al final de la lista
    check("1\n2\n91125426\n911\n", "NO\n")


if __name__ == "__main__":
    if not SUBMIT:
        run_tests()
    else:
        lines = sys.stdin.read().strip().splitlines()
        i = 0
        t = int(lines[i]); i += 1
        results = []
        for _ in range(t):
            n = int(lines[i]); i += 1
            numbers = []
            for _ in range(n):
                numbers.append(lines[i]); i += 1
            results.append("YES" if is_consistent(numbers) else "NO")
        print("\n".join(results))
