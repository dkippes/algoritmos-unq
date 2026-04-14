import sys
input = sys.stdin.readline

# UVA 12506 - Shortest Names
# Dado un conjunto de nombres (ningun nombre es prefijo de otro),
# encontrar la longitud del prefijo unico mas corto de cada nombre y sumarlas.
#
# Tecnica: Trie donde cada nodo guarda cuantas palabras pasan por el.
# El prefijo unico mas corto de un nombre es la profundidad del primer
# nodo con count == 1 en su camino.
#
# Ejemplo con: "aaaaa", "bbb", "abababab"
#
#                root
#               /    \
#             a(2)   b(1) <-- count=1, prefijo de "bbb" = "b" (len=1)
#            /    \     \
#          a(1)  b(1)   b(1)
#          /\*    \*      \
#        ...  ...  ...   b(1)
#
#   * count=1 => prefijo unico encontrado
#
#   "aaaaa"    -> root -> a(2) -> a(1)*  => len=2  llama "aa"
#   "bbb"      -> root -> b(1)*          => len=1  llama "b"
#   "abababab" -> root -> a(2) -> b(1)*  => len=2  llama "ab"
#                                          total = 5
#
# Ejecutar: echo "1\n3\naaaaa\nbbb\nabababab" | python3 12506.py
# Link Juez: https://vjudge.net/problem/UVA-12506

SUBMIT = False  # cambiar a True para enviar al juez


class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0  # cuantas palabras pasan por este nodo


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            node.count += 1

    def shortest_prefix_len(self, word):
        node = self.root
        for depth, ch in enumerate(word, 1):
            node = node.children[ch]
            if node.count == 1:
                return depth
        return len(word)


def solve(names):
    trie = Trie()
    for name in names:
        trie.insert(name)
    return sum(trie.shortest_prefix_len(name) for name in names)


def run(input_str):
    lines = input_str.strip().splitlines()
    idx = 0
    t = int(lines[idx]); idx += 1
    results = []
    for _ in range(t):
        n = int(lines[idx]); idx += 1
        names = [lines[idx + i] for i in range(n)]
        idx += n
        results.append(str(solve(names)))
    return "\n".join(results) + "\n"


def run_tests():
    def check(input_str, expected):
        got = run(input_str)
        if got == expected:
            print("PASS")
        else:
            print(f"FAIL\n  esperado: {repr(expected)}\n  obtenido: {repr(got)}")

    # Caso del enunciado: aaaaa->aaa(3), bbb->b(1), abababab->ab(2) => 5 (espera 5)
    check("1\n3\naaaaa\nbbb\nabababab\n", "5\n")

    # Un solo nombre: prefijo minimo es 1 caracter
    check("1\n1\nabc\n", "1\n")

    # Nombres completamente distintos en primer caracter
    check("1\n3\nabc\nbcd\ncde\n", "3\n")

    # Prefijos mas largos necesarios
    check("1\n2\nab\nac\n", "4\n")

    # Multiples casos
    check("2\n1\nhello\n3\naaaaa\nbbb\nabababab\n", "1\n5\n")


if __name__ == "__main__":
    if not SUBMIT:
        run_tests()
    else:
        data = sys.stdin.read()
        print(run(data), end="")
