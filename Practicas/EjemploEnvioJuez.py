## EJEMPLO DE COMO MANDARLO AL JUEZ
import sys

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

if __name__ == "__main__":
        data = sys.stdin.read().splitlines()
        text = data[0]
        pattern = data[1]
        print(count_occurrences(text, pattern))