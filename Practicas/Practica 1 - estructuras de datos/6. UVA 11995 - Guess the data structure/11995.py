import sys
from collections import deque
import heapq

# UVA 11995 - I Can Guess the Data Structure
# Dada una secuencia de inserciones (1 x) y extracciones (2 x),
# determinar si es consistente con stack, queue, priority queue, ambas o ninguna.
#
# Ejecutar: echo "6\n1 1\n1 2\n1 3\n2 1\n2 2\n2 3" | python3 11995.py

SUBMIT = False  # cambiar a True para enviar al juez


def solve(ops):
    stack = []
    queue = deque()
    pq = []  # max-heap con negativos

    is_stack = True
    is_queue = True
    is_pq    = True

    for operation, value in ops:
        if operation == 1:
            stack.append(value)
            queue.append(value)
            heapq.heappush(pq, -value) # Lo guarda como negativo porque saca el menor primero
        else:
            if is_stack:
                if not stack or stack[-1] != value:
                    is_stack = False
                else:
                    stack.pop()

            if is_queue:
                if not queue or queue[0] != value:
                    is_queue = False
                else:
                    queue.popleft()

            if is_pq:
                if not pq or -pq[0] != value:
                    is_pq = False
                else:
                    heapq.heappop(pq) # Saca el menor de todos

    count = sum([is_stack, is_queue, is_pq])
    if count == 0:
        return "impossible"
    if count > 1:
        return "not sure"
    if is_stack: return "stack"
    if is_queue: return "queue"
    return "priority queue"


def run(input_str):
    output = []
    tokens = input_str.split()
    idx = 0
    while idx < len(tokens):
        n = int(tokens[idx]); idx += 1
        ops = []
        for _ in range(n):
            operation = int(tokens[idx]); idx += 1
            value = int(tokens[idx]); idx += 1
            ops.append((operation, value))
        output.append(solve(ops))
    return "\n".join(output) + "\n"


def run_tests():
    def check(input_str, expected):
        got = run(input_str)
        if got == expected:
            print("PASS")
        else:
            print(f"FAIL\n  esperado: {repr(expected)}\n  obtenido: {repr(got)}")

    # Inserta 1,2,3 y saca 1,2,3 -> FIFO -> queue
    check("6\n1 1\n1 2\n1 3\n2 1\n2 2\n2 3\n", "queue\n")

    # Inserta 1,2,3 y saca 3,2,1 -> compatible con stack y pq -> not sure
    check("6\n1 1\n1 2\n1 3\n2 3\n2 2\n2 1\n", "not sure\n")

    # Inserta 1 y saca 2 -> ninguna estructura da eso -> impossible
    check("2\n1 1\n2 2\n", "impossible\n")

    # Inserta 2,1 y saca 1,2 -> LIFO -> stack
    check("4\n1 2\n1 1\n2 1\n2 2\n", "stack\n")

    # Inserta 2,5,1,3 saca 5, inserta 4, saca 4 -> siempre el mayor -> priority queue
    check("7\n1 2\n1 5\n1 1\n1 3\n2 5\n1 4\n2 4\n", "priority queue\n")


if __name__ == "__main__":
    if not SUBMIT:
        run_tests()
    else:
        tokens = sys.stdin.read().split()
        idx = 0
        while idx < len(tokens):
            n = int(tokens[idx]); idx += 1
            ops = []
            for _ in range(n):
                operation = int(tokens[idx]); idx += 1
                value = int(tokens[idx]); idx += 1
                ops.append((operation, value))
            print(solve(ops))
