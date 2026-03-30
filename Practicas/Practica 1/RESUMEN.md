# Practica 1 — Resumen de Teoría

**Fuentes:** Laaksonen (Guide to Competitive Programming, 2017), Skiena (The Algorithm Design Manual, 2nd ed.), Cormen et al. (Introduction to Algorithms, 3rd ed. — CLRS), Halim et al. (Competitive Programming 4)

---

## 1. ¿Qué es la Programación Competitiva?

### Definición (Laaksonen, Cap. 1)

> "Competitive programming combines two topics: the design of algorithms and the implementation of algorithms."
> — Laaksonen, *Guide to Competitive Programming*, p. 1

La programación competitiva une dos cosas:

1. **Diseño de algoritmos**: inventar algoritmos eficientes que resuelvan problemas computacionales bien definidos. Requiere habilidad para resolver problemas y pensamiento matemático.

2. **Implementación de algoritmos**: en las competencias, las soluciones se evalúan ejecutando el programa con casos de prueba (*test cases*). Si pasa todos, se acepta. No alcanza con describir la idea — hay que implementarla correctamente.

Una diferencia clave con la ciencia teórica: un científico escribe una demostración para probar que su algoritmo funciona; un programador competitivo **implementa** el algoritmo y lo somete al juez automático.

### Principales competencias (Laaksonen, Sección 1.1.1)

- **IOI** (International Olympiad in Informatics): para estudiantes secundarios. Dos concursos de 5 horas, tres problemas difíciles cada uno. Aproximadamente 300 participantes de 80 países.

- **ICPC** (International Collegiate Programming Contest): para universitarios. Equipos de tres estudiantes, una sola computadora. Cinco horas para resolver ~10 problemas. Miles de equipos a nivel mundial; llegar a la final es un logro en sí mismo.

- **Concursos online**: Codeforces (semanal), AtCoder, CodeChef, HackerRank, Topcoder. También hay concursos corporativos: Facebook Hacker Cup, Google Code Jam, Yandex.Algorithm.

### El lenguaje más usado

Laaksonen señala que en Google Code Jam 2017, entre los mejores 3000 participantes, el 79% usó C++, el 16% Python y el 8% Java. C++ es la elección predominante porque es muy eficiente y su biblioteca estándar contiene estructuras de datos y algoritmos listos para usar.

### Consejos para practicar (Laaksonen, Sección 1.1.2)

- La **calidad** de los problemas resueltos importa más que la cantidad. Es tentador elegir problemas fáciles y saltearse los difíciles, pero el verdadero progreso viene de enfrentar los difíciles.
- La mayoría de los problemas de competencia se resuelven con algoritmos simples y cortos; la dificultad está en **inventar** el algoritmo, no en memorizarlo.
- Implementar correctamente y sin bugs es una habilidad valiosa en sí misma.

### Jueces online

El modelo estándar es: enviás tu código, el juez lo compila y ejecuta con casos de prueba ocultos. Si pasa todos en tiempo y memoria, obtenés "Accepted" (AC). Los veredictos posibles incluyen: Wrong Answer (WA), Time Limit Exceeded (TLE), Runtime Error (RE), etc.

---

## 2. Complejidad Algorítmica — Big-O

### ¿Por qué no medir en segundos?

El tiempo de ejecución en segundos depende de la computadora, el compilador, la carga del sistema, etc. Necesitamos una medida independiente del hardware que capture **cómo crece el tiempo en función del tamaño del input**.

Tal como explica CLRS (Cap. 2): el tiempo de ejecución de un algoritmo sobre un input particular es el número de *pasos primitivos* ejecutados. Para abstraer los detalles, usamos un modelo de computación (la **RAM model**): cada instrucción aritmética, de movimiento de datos o de control toma una cantidad constante de tiempo.

### El concepto de "orden de crecimiento" (CLRS, Cap. 2.2)

> "It is the **rate of growth**, or **order of growth**, of the running time that really interests us. We therefore consider only the leading term of a formula, since the lower-order terms are relatively insignificant for large values of n."
> — Cormen et al., *Introduction to Algorithms*, 3rd ed., p. 27

Por ejemplo, si el peor caso de insertion sort es T(n) = an² + bn + c (para constantes a, b, c), ignoramos los términos de menor orden y el coeficiente del término dominante. Quedamos con **Θ(n²)** — insertion sort es cuadrático.

### Definiciones formales (CLRS, Sección 3.1)

Estas tres notaciones describen el comportamiento asintótico de funciones:

#### Θ-notación (cota exacta)

Para una función g(n), **Θ(g(n))** es el conjunto de funciones:

```
Θ(g(n)) = { f(n) : existen constantes positivas c₁, c₂, n₀ tal que
              0 ≤ c₁·g(n) ≤ f(n) ≤ c₂·g(n)  para todo n ≥ n₀ }
```

Intuitivamente: f(n) = Θ(g(n)) significa que f(n) crece **exactamente como** g(n) salvo por factores constantes. Se dice que g(n) es una *cota asintóticamente ajustada* para f(n).

**Ejemplo:** ½n² - 3n = Θ(n²). Tomando c₁ = 1/14, c₂ = 1/2 y n₀ = 7, se puede verificar que 0 ≤ (1/14)n² ≤ ½n² - 3n ≤ (1/2)n² para todo n ≥ 7.

#### O-notación (cota superior)

```
O(g(n)) = { f(n) : existen constantes positivas c, n₀ tal que
             0 ≤ f(n) ≤ c·g(n)  para todo n ≥ n₀ }
```

> "We use O-notation to give an upper bound on a function, to within a constant factor."
> — Cormen et al., CLRS, p. 47

**Importante:** f(n) = Θ(g(n)) implica f(n) = O(g(n)), pero no al revés. Por ejemplo, n = O(n²) es correcto aunque no sea ajustado.

#### Ω-notación (cota inferior)

```
Ω(g(n)) = { f(n) : existen constantes positivas c, n₀ tal que
             0 ≤ c·g(n) ≤ f(n)  para todo n ≥ n₀ }
```

**Teorema 3.1 (CLRS):** Para cualesquiera dos funciones f(n) y g(n):

> f(n) = Θ(g(n)) **si y solo si** f(n) = O(g(n)) **y** f(n) = Ω(g(n))

### La misma idea en palabras de Skiena

Skiena (Cap. 2) da una visión más intuitiva de las notaciones:

> "The Big Oh notation provides for a rough notion of equality when comparing functions."
> — Skiena, *The Algorithm Design Manual*, 2nd ed., p. 36

Skiena ilustra con el ejemplo de 3n² - 100n + 6:

- **3n² - 100n + 6 = O(n²)** porque eligiendo c = 3: 3n² > 3n² - 100n + 6
- **3n² - 100n + 6 = Ω(n²)** porque eligiendo c = 2: 2n² < 3n² - 100n + 6 cuando n > 100
- **3n² - 100n + 6 = Θ(n²)** porque valen ambas, O y Ω

También se puede expresar como: **f(n) = O(g(n))** si existe una constante c tal que f(n) ≤ c·g(n) para n suficientemente grande. En la práctica descartamos las constantes multiplicativas porque como muestra la tabla de tiempos de Skiena, para n grande **el orden de crecimiento domina absolutamente** cualquier constante.

### Definición informal de Laaksonen (Sección 3.1.4)

> "What does it exactly mean that an algorithm works in O(f(n)) time? It means that there are constants c and n₀ such that the algorithm performs at most c·f(n) operations for all inputs where n ≥ n₀."
> — Laaksonen, p. 32

Y sobre las otras notaciones:
- **Ω(f(n))**: el algoritmo realiza **al menos** c·f(n) operaciones para n ≥ n₀.
- **Θ(f(n))**: es tanto O(f(n)) como Ω(f(n)) — cota ajustada.

---

## 3. Cómo Estimar la Complejidad de un Algoritmo

### Reglas de cálculo (Laaksonen, Sección 3.1.1)

**Regla 1 — Un loop simple:**
```c
for (int i = 1; i <= n; i++) {
    // operación O(1)
}
// Complejidad: O(n)
```

**Regla 2 — Dos loops anidados:**
```c
for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= n; j++) {
        // operación O(1)
    }
}
// Complejidad: O(n²)
```

En general, k loops anidados que cada uno recorre n valores → **O(nᵏ)**.

**Regla 3 — Loop triangular:**
```c
for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= i; j++) {
        // operación O(1)
    }
}
// El loop interno ejecuta 1+2+...+n = n(n+1)/2 veces → O(n²)
```

**Regla 4 — Fases consecutivas (no anidadas):**
La complejidad total es la de la fase más lenta (el cuello de botella). Si hay fases O(n), O(n²) y O(n) consecutivas, el total es **O(n²)**.

**Regla 5 — Descartamos constantes y términos menores:**
```
O(3n² + 5n + 7)  →  O(n²)
O(n/2)           →  O(n)
```

La complejidad no dice el número exacto de operaciones, solo el **orden de crecimiento**.

**Regla 6 — Funciones recursivas:**

La complejidad depende de cuántas veces se llama la función y cuánto tarda cada llamada.

```c
void f(int n) {
    if (n == 1) return;
    f(n-1);
}
// f(n) genera n llamadas → O(n)
```

```c
void g(int n) {
    if (n == 1) return;
    g(n-1);
    g(n-1);
}
// Genera 2^(n-1) llamadas: 1+2+4+...+2^(n-1) = 2^n - 1 → O(2^n)
```

### Análisis de insertion sort (CLRS, Sección 2.2)

CLRS analiza detalladamente insertion sort como ejemplo:

- **Mejor caso** (array ya ordenado): cada elemento se inserta en O(1) → T(n) = O(n).
- **Peor caso** (array en orden inverso): cada elemento i se compara con todos los anteriores → T(n) = an² + bn + c → **Θ(n²)**.

```c
// Insertion sort — peor caso O(n²)
for (int j = 2; j <= n; j++) {
    int key = A[j];
    int i = j - 1;
    while (i > 0 && A[i] > key) {
        A[i+1] = A[i];
        i--;
    }
    A[i+1] = key;
}
```

Skiena hace la misma observación para insertion sort con un análisis más informal: el loop exterior corre n veces, el loop interior hasta n veces en peor caso → O(n²).

### La importancia de analizar antes de codear

Skiena relata en su "war story" cómo un algoritmo O(n²) para n = 10⁹ era completamente inviable, mientras que mejorarlo a O(n^(4/3) · log n) lo hizo ~30,000 veces más rápido. La mejora algorítmica fue mucho más impactante que comprar hardware más rápido.

---

## 4. Complejidades Comunes y Límites Prácticos

### Las complejidades más frecuentes (Laaksonen, Sección 3.1.2)

| Complejidad | Nombre | Cómo aparece |
|-------------|--------|--------------|
| **O(1)** | Constante | Fórmula directa, acceso a array por índice |
| **O(log n)** | Logarítmica | Búsqueda binaria: se divide el espacio a la mitad en cada paso |
| **O(√n)** | Raíz cuadrada | Algoritmos que dividen en bloques de √n elementos |
| **O(n)** | Lineal | Recorrer el input una cantidad constante de veces |
| **O(n log n)** | Lineal-logarítmica | Algoritmos de sorting eficientes (merge sort), o usar una estructura O(log n) n veces |
| **O(n²)** | Cuadrática | Dos loops anidados; procesar todos los pares |
| **O(n³)** | Cúbica | Tres loops anidados; procesar todos los tríos |
| **O(2ⁿ)** | Exponencial | Iterar sobre todos los subconjuntos del input |
| **O(n!)** | Factorial | Iterar sobre todas las permutaciones del input |

Un algoritmo es **polinomial** si su complejidad es a lo sumo O(nᵏ) para alguna constante k. Los problemas NP-hard son aquellos para los que no se conoce ningún algoritmo polinomial.

### Tabla de crecimiento (Skiena, p. 38)

Esta tabla (adaptada de Skiena) muestra cuánto tarda cada complejidad en una computadora que ejecuta 1 operación por nanosegundo:

| n | O(log n) | O(n) | O(n log n) | O(n²) | O(2ⁿ) |
|---|----------|------|-----------|-------|--------|
| 10 | ~0.003 μs | ~0.01 μs | ~0.033 μs | ~0.1 μs | ~1 μs |
| 100 | ~0.007 μs | ~0.1 μs | ~0.644 μs | ~10 μs | ≈4×10¹³ años |
| 1,000 | ~0.010 μs | ~1 μs | ~9.9 μs | ~1 ms | — |
| 10,000 | ~0.013 μs | ~10 μs | ~130 μs | ~100 ms | — |
| 1,000,000 | ~0.020 μs | ~1 ms | ~19.9 ms | ~16.7 min | — |

Conclusiones (Skiena):
- Para n = 10, todos los algoritmos son prácticamente iguales.
- Para n grande, el orden de crecimiento lo determina todo.
- Los algoritmos O(2ⁿ) son inviables para n > ~25-30.

### Límites prácticos para competencias (Laaksonen, Sección 3.1.3)

> "The starting point for estimations is the fact that a modern computer can perform some hundreds of millions of simple operations in a second."
> — Laaksonen, p. 31

Con un límite de tiempo típico de **1 segundo** en jueces online:

| Tamaño del input n | Complejidad esperada |
|--------------------|----------------------|
| n ≤ 10 | O(n!) |
| n ≤ 20 | O(2ⁿ) |
| n ≤ 500 | O(n³) |
| n ≤ 5.000 | O(n²) |
| n ≤ 10⁶ | O(n log n) o O(n) |
| n muy grande | O(1) o O(log n) |

**Uso práctico:** Si el enunciado dice n ≤ 10⁵, casi seguro se espera O(n log n) o O(n). Saber esto antes de codear te guía hacia el algoritmo correcto y descarta los ineficientes.

**Ejemplo concreto (Laaksonen):** Con n = 10⁵ y tiempo límite 1 segundo:
- O(n²) haría (10⁵)² = 10¹⁰ operaciones → demasiado lento (decenas de segundos).
- O(n log n) haría ~10⁵ × log₂(10⁵) ≈ 1.6 × 10⁶ operaciones → entra con holgura.

### Ejemplo práctico: subarray de suma máxima (Laaksonen, Sección 3.2.1)

Dado un array de n números (posiblemente negativos), encontrar la subsecuencia contigua con suma máxima.

Tres soluciones con complejidades diferentes:

```c
// O(n³) — Fuerza bruta
int best = 0;
for (int a = 0; a < n; a++) {
    for (int b = a; b < n; b++) {
        int sum = 0;
        for (int k = a; k <= b; k++) {
            sum += array[k];
        }
        best = max(best, sum);
    }
}

// O(n²) — Eliminar un loop
int best = 0;
for (int a = 0; a < n; a++) {
    int sum = 0;
    for (int b = a; b < n; b++) {
        sum += array[b];
        best = max(best, sum);
    }
}

// O(n) — Algoritmo de Kadane
int best = 0, sum = 0;
for (int k = 0; k < n; k++) {
    sum = max(array[k], sum + array[k]);
    best = max(best, sum);
}
```

Laaksonen muestra la tabla de tiempos reales en su computadora:

| n | O(n³) | O(n²) | O(n) |
|---|--------|--------|------|
| 10² | 0.0 s | 0.0 s | 0.0 s |
| 10³ | 0.1 s | 0.0 s | 0.0 s |
| 10⁴ | >10 s | 0.1 s | 0.0 s |
| 10⁵ | >10 s | 5.3 s | 0.0 s |
| 10⁶ | >10 s | >10 s | 0.0 s |

La diferencia es dramática: solo el O(n) procesa los inputs grandes instantáneamente.

---

## 5. Estructuras de Datos

Una estructura de datos es una forma de organizar información para que ciertas operaciones sean eficientes. La elección de la estructura adecuada puede ser la diferencia entre un algoritmo O(n²) y uno O(n log n).

Como establece CLRS en la introducción a la Parte III:

> "Algorithms may require several different types of operations to be performed on sets. For example, many algorithms need only the ability to insert elements into, delete elements from, and test membership in a set. We call a dynamic set that supports these operations a **dictionary**."
> — Cormen et al., CLRS, p. 229

Las operaciones típicas sobre conjuntos dinámicos son: `SEARCH`, `INSERT`, `DELETE`, `MINIMUM`, `MAXIMUM`, `SUCCESSOR`, `PREDECESSOR`.

---

### 5.1 Arrays (Arreglos)

La estructura más fundamental. Elementos almacenados en posiciones contiguas de memoria.

```c
int arr[5] = {10, 20, 30, 40, 50};
arr[2];  // → 30, acceso O(1) por índice
```

**Característica clave:** el acceso por índice es O(1) porque la dirección de memoria de `arr[i]` se calcula directamente como `dirección_base + i × tamaño_elemento`.

| Operación | Complejidad |
|-----------|-------------|
| Acceso por índice | O(1) |
| Búsqueda de un valor | O(n) |
| Insertar al final | O(1) amortizado (con arrays dinámicos) |
| Insertar en el medio | O(n) — hay que desplazar elementos |
| Borrar en el medio | O(n) — hay que desplazar elementos |

**Cuándo usarlo:** cuando el tamaño es fijo o se sabe de antemano, y se necesita acceso rápido por índice.

#### Array dinámico (vector en C++)

Laaksonen (Cap. 5.1) describe el vector como un array dinámico que permite agregar y quitar elementos al final eficientemente:

```cpp
vector<int> v;
v.push_back(3);  // [3]
v.push_back(2);  // [3,2]
v.push_back(5);  // [3,2,5]
cout << v[0];    // 3 — acceso O(1)
cout << v.size(); // 3
v.pop_back();    // [3,2] — O(1) amortizado
```

`push_back` y `pop_back` trabajan en O(1) **amortizado**. En la práctica, usar un vector es casi tan rápido como un array estático.

---

### 5.2 Listas Enlazadas (Linked Lists)

CLRS (Sección 10.2) describe las listas enlazadas como estructuras donde los elementos se almacenan en nodos, y cada nodo tiene un puntero al siguiente (y al anterior en listas doblemente enlazadas).

> "A linked list is a data structure in which the objects are arranged in a linear order. Unlike an array, however, in which the linear order is determined by the array indices, the order in a linked list is determined by a **pointer** in each object."
> — Cormen et al., CLRS, p. 236

```
[10 | →] → [20 | →] → [30 | →] → NULL
 head
```

En una lista **doblemente enlazada**, cada nodo tiene `key`, `next` y `prev`. Las operaciones básicas son:

- **LIST-SEARCH(L, k):** busca linealmente → **Θ(n)** en peor caso.
- **LIST-INSERT(L, x):** inserta al principio en **O(1)**.
- **LIST-DELETE(L, x):** dado el puntero al nodo, borra en **O(1)**. Pero si hay que buscarlo primero, es **Θ(n)**.

| Operación | Complejidad |
|-----------|-------------|
| Acceso por índice | O(n) |
| Búsqueda | O(n) |
| Insertar al inicio (con puntero) | O(1) |
| Insertar en el medio (con puntero) | O(1) |
| Borrar (con puntero al nodo) | O(1) |

**Cuándo usarla:** cuando se necesita insertar/borrar frecuentemente en posiciones arbitrarias y ya se tiene el puntero al nodo. En la práctica de competitive programming se usa poco directamente — el `deque` y el `list` de C++ cubren estos casos.

---

### 5.3 Stack (Pila)

CLRS (Sección 10.1) define el stack como una estructura **LIFO** (*Last In, First Out*): el último elemento insertado es el primero en salir. Es como una pila de platos — solo se puede tomar el de arriba.

Las operaciones básicas son `PUSH` (insertar) y `POP` (sacar). Ambas trabajan en **O(1)**.

```cpp
stack<int> s;
s.push(2);            // [2]
s.push(5);            // [2, 5]
cout << s.top();      // 5 — el tope, O(1)
s.pop();              // [2]
cout << s.top();      // 2
```

Laaksonen (Sección 5.1.3) menciona que en C++ el `stack` se basa por defecto en un `deque` y todas las operaciones son O(1).

| Operación | Complejidad |
|-----------|-------------|
| push | O(1) |
| pop | O(1) |
| top (ver el tope) | O(1) |

**Cuándo usarlo:** procesamiento en orden inverso (ej: validar paréntesis balanceados, DFS iterativo, backtracking, evaluar expresiones).

---

### 5.4 Queue (Cola)

**FIFO** (*First In, First Out*): el primero en entrar es el primero en salir. Como una fila del supermercado.

CLRS (Sección 10.1) describe las operaciones `ENQUEUE` (insertar al final) y `DEQUEUE` (sacar del frente), ambas en **O(1)** usando un array circular.

```cpp
queue<int> q;
q.push(2);              // [2]
q.push(5);              // [2, 5]
cout << q.front();      // 2 — el primero
q.pop();                // [5]
cout << q.back();       // 5 — el último
```

| Operación | Complejidad |
|-----------|-------------|
| push (enqueue) | O(1) |
| pop (dequeue) | O(1) |
| front / back | O(1) |

**Cuándo usarla:** BFS (Breadth-First Search), simulaciones donde se procesan elementos en orden de llegada.

#### Deque (double-ended queue)

Laaksonen (Sección 5.1.3) menciona el `deque` de C++ como extensión de la cola: permite insertar y sacar por **ambos extremos** en O(1). Útil cuando se necesita flexibilidad en ambos lados.

```cpp
deque<int> d;
d.push_back(5);    // [5]
d.push_front(3);   // [3, 5]
d.pop_front();     // [5]
d.pop_back();      // []
```

---

### 5.5 Set (Conjunto)

Laaksonen (Sección 5.2.1) describe dos versiones en C++:

- **`set<T>`**: basado en árbol binario balanceado (red-black tree). Operaciones en **O(log n)**. Los elementos se mantienen **ordenados**.
- **`unordered_set<T>`**: basado en hash table. Operaciones en **O(1) promedio**, pero sin orden.

```cpp
set<int> s;
s.insert(3);
s.insert(2);
s.insert(5);
s.insert(2);          // no se inserta (ya existe)
// s contiene: {2, 3, 5}

cout << s.count(3);   // 1 (existe)
cout << s.count(4);   // 0 (no existe)
s.erase(3);           // borra 3

// Iteración en orden ascendente:
for (auto x : s) cout << x << "\n";  // 2 5
```

Propiedad importante: **todos los elementos son distintos**. `count()` devuelve siempre 0 o 1.

```cpp
// lower_bound y upper_bound — O(log n)
auto it = s.lower_bound(x);  // primer elemento >= x
auto it = s.upper_bound(x);  // primer elemento > x
```

| Operación | set<T> | unordered_set<T> |
|-----------|--------|-----------------|
| Insertar | O(log n) | O(1) promedio |
| Buscar | O(log n) | O(1) promedio |
| Borrar | O(log n) | O(1) promedio |
| Mínimo / Máximo | O(log n) | No disponible |
| lower_bound | O(log n) | No disponible |

**Cuándo usarlo:** cuando necesitás saber si un elemento ya existe, mantener elementos únicos, o acceder al mínimo/máximo rápidamente.

#### Multiset

Permite **múltiples copias** del mismo valor. `count(x)` devuelve cuántas veces aparece x. Cuidado: `erase(x)` borra **todas** las copias. Para borrar solo una: `s.erase(s.find(x))`.

---

### 5.6 Map (Diccionario)

Laaksonen (Sección 5.2.2) describe el map como un conjunto de pares clave-valor. Se puede ver como un array generalizado donde las claves pueden ser de cualquier tipo.

- **`map<K,V>`**: árbol binario balanceado. Acceso en O(log n). Claves ordenadas.
- **`unordered_map<K,V>`**: hash table. Acceso en O(1) promedio. Sin orden.

```cpp
map<string, int> m;
m["monkey"] = 4;
m["banana"] = 3;
m["harpsichord"] = 9;
cout << m["banana"];   // 3 — O(log n)

// Si la clave no existe, se crea con valor por defecto:
cout << m["aybabtu"];  // 0 (crea la entrada)

// Verificar si una clave existe:
if (m.count("monkey")) {
    // existe
}

// Iterar (en orden de clave):
for (auto x : m) {
    cout << x.first << " " << x.second << "\n";
}
```

| Operación | map<K,V> | unordered_map<K,V> |
|-----------|----------|--------------------|
| Insertar | O(log n) | O(1) promedio |
| Buscar | O(log n) | O(1) promedio |
| Borrar | O(log n) | O(1) promedio |

**Cuándo usarlo:** contar frecuencias, cachear resultados, asociar cualquier clave con un valor.

```cpp
// Ejemplo: contar frecuencia de palabras
map<string, int> freq;
string word;
while (cin >> word) {
    freq[word]++;
}
```

---

### 5.7 Priority Queue (Cola de Prioridad / Heap)

Laaksonen (Sección 5.2.3) la describe como una estructura multiset que soporta inserción y extracción del **mínimo o máximo**. Está basada internamente en un **heap** (árbol binario especial).

> "While a multiset provides all the operations of a priority queue and more, the benefit of using a priority queue is that it has smaller constant factors."
> — Laaksonen, p. 58

CLRS (Cap. 6) explica los heaps en detalle: un **max-heap** tiene la propiedad de que cada nodo es mayor o igual que sus hijos. El máximo siempre está en la raíz. Las operaciones de inserción y extracción mantienen esta propiedad ajustando el árbol en O(log n).

```cpp
// Por defecto: max-heap (sale el mayor)
priority_queue<int> pq;
pq.push(3);
pq.push(5);
pq.push(7);
pq.push(2);
cout << pq.top();  // 7
pq.pop();
cout << pq.top();  // 5

// Min-heap (sale el menor):
priority_queue<int, vector<int>, greater<int>> min_pq;
```

| Operación | Complejidad |
|-----------|-------------|
| push | O(log n) |
| pop | O(log n) |
| top (ver el máximo/mínimo) | O(1) |

**Cuándo usarla:** cuando necesitás siempre el elemento de mayor o menor prioridad (algoritmo de Dijkstra, scheduling, simulaciones de eventos).

---

### 5.8 Árbol Binario de Búsqueda (BST)

CLRS (Cap. 12) define el árbol binario de búsqueda:

> "The search tree data structure supports many dynamic-set operations, including SEARCH, MINIMUM, MAXIMUM, PREDECESSOR, SUCCESSOR, INSERT, and DELETE."
> — Cormen et al., CLRS, p. 286

**Propiedad BST:** Para cualquier nodo x, todos los nodos en el subárbol izquierdo tienen clave ≤ x.key, y todos en el subárbol derecho tienen clave ≥ x.key.

```
        6
       / \
      5   7
     / \   \
    2   5   8
```

Las operaciones básicas (SEARCH, INSERT, DELETE, MINIMUM, MAXIMUM, SUCCESSOR, PREDECESSOR) toman tiempo proporcional a la **altura** del árbol h.

- En un árbol completo de n nodos: h = O(log n) → operaciones en **Θ(log n)**.
- En el peor caso (árbol degenerado, como una lista): h = n → operaciones en **Θ(n)**.

Para un BST construido aleatoriamente, la altura esperada es O(log n). Pero como no siempre podemos garantizar inputs aleatorios, se usan variantes balanceadas.

#### Red-Black Trees (CLRS, Cap. 13)

Los **árboles red-black** son BST con restricciones adicionales que garantizan que el árbol permanezca balanceado. **Garantizan O(log n) en el peor caso** para todas las operaciones. Son la implementación interna de `set` y `map` en C++.

> "Unlike ordinary binary search trees, red-black trees are guaranteed to perform well: operations take O(lg n) time in the worst case."
> — Cormen et al., CLRS, p. 231

---

### 5.9 Hash Tables

CLRS (Cap. 11) presenta las tablas hash como la implementación eficiente de diccionarios:

> "Although searching for an element in a hash table can take as long as searching for an element in a linked list — Θ(n) time in the worst case — in practice, hashing performs extremely well. Under reasonable assumptions, the average time to search for an element in a hash table is O(1)."
> — Cormen et al., CLRS, p. 253

**Idea:** una función hash h(k) mapea la clave k a un índice del array. En lugar de acceder a T[k] directamente (lo cual requeriría un array de tamaño |U|), accedemos a T[h(k)].

Problema: dos claves pueden mapearse al mismo índice → **colisión**. Se resuelve con:
- **Chaining**: cada slot tiene una lista enlazada de elementos con el mismo hash.
- **Open addressing**: si hay colisión, se busca otro slot disponible.

| Operación | Promedio | Peor caso |
|-----------|----------|-----------|
| Buscar | O(1) | O(n) |
| Insertar | O(1) | O(n) |
| Borrar | O(1) | O(n) |

El peor caso O(n) ocurre si todas las claves hashean al mismo slot, pero bajo supuestos razonables de hashing uniforme, el promedio es O(1).

En C++: `unordered_set<T>` y `unordered_map<K,V>`.

---

### 5.10 Sorting (Ordenamiento)

Laaksonen (Secciones 4.1) presenta tres algoritmos de sorting importantes:

#### Bubble Sort — O(n²)

```c
for (int i = 0; i < n; i++) {
    for (int j = 0; j < n-1; j++) {
        if (array[j] > array[j+1]) {
            swap(array[j], array[j+1]);
        }
    }
}
```

Concepto clave: una **inversión** es un par (a, b) con a < b pero array[a] > array[b]. Cada swap elimina exactamente una inversión. En el peor caso hay n(n-1)/2 inversiones → O(n²) swaps obligatorios para cualquier algoritmo que solo swapee elementos consecutivos.

#### Merge Sort — O(n log n)

Basado en recursión (divide y vencerás):
1. Si el subarray tiene 1 elemento, ya está ordenado.
2. Calcular el punto medio k.
3. Ordenar recursivamente la mitad izquierda.
4. Ordenar recursivamente la mitad derecha.
5. Mergear las dos mitades ordenadas en O(n).

Hay O(log n) niveles de recursión, y en cada nivel se hace O(n) trabajo total → **O(n log n)**.

#### Lower bound de sorting — Ω(n log n)

Laaksonen demuestra que no se puede ordenar más rápido que O(n log n) usando comparaciones. El argumento: el proceso de sorting es un árbol de decisión con n! hojas (una por cada permutación posible). La altura mínima de ese árbol es log₂(n!) = Ω(n log n).

#### Counting Sort — O(n)

No usa comparaciones. Asume que los elementos son enteros entre 0 y c:

```c
// Contar ocurrencias y reconstruir
int count[c+1] = {0};
for (int i = 0; i < n; i++) count[array[i]]++;
// Reconstruir el array en orden
```

O(n) pero solo funciona cuando c = O(n).

#### Sorting en la práctica (C++)

```cpp
// Ordena en O(n log n) — usar siempre que sea posible
sort(array, array + n);          // array estático
sort(v.begin(), v.end());        // vector

// Orden descendente:
sort(v.begin(), v.end(), greater<int>());

// Con criterio personalizado:
sort(v.begin(), v.end(), [](int a, int b) {
    return a > b;
});
```

#### Binary Search — O(log n)

Laaksonen (Sección 4.3) presenta la búsqueda binaria para encontrar un elemento en un array **ordenado**:

```c
int a = 0, b = n - 1;
while (a <= b) {
    int k = (a + b) / 2;
    if (array[k] == x) {
        // encontrado en índice k
    }
    if (array[k] < x) a = k + 1;
    else b = k - 1;
}
```

En cada paso se descarta la mitad del subarray activo → O(log n). La búsqueda binaria en un directorio de un millón de nombres requiere solo **20 comparaciones** (log₂ 1,000,000 ≈ 20). Skiena lo destaca como "one of the most powerful ideas in algorithm design."

---

## 6. Tabla Comparativa Final

| Estructura | Acceso idx | Búsqueda | Inserción | Borrado | Cuándo usarla |
|------------|-----------|----------|-----------|---------|---------------|
| Array | O(1) | O(n) | O(n) | O(n) | Tamaño fijo, acceso por índice |
| Vector (C++) | O(1) | O(n) | O(1) amort. (final) | O(n) | Array dinámico general |
| Linked List | O(n) | O(n) | O(1) con puntero | O(1) con puntero | Inserciones frecuentes en medio |
| Stack | — | — | O(1) | O(1) | LIFO: DFS, paréntesis, backtrack |
| Queue | — | — | O(1) | O(1) | FIFO: BFS, simulaciones |
| Set (BST) | — | O(log n) | O(log n) | O(log n) | Sin repetidos, con orden |
| unordered_set | — | O(1) prom | O(1) prom | O(1) prom | Sin repetidos, sin orden |
| Map (BST) | — | O(log n) | O(log n) | O(log n) | Clave→valor, con orden |
| unordered_map | — | O(1) prom | O(1) prom | O(1) prom | Clave→valor, sin orden |
| Priority Queue | O(1) top | — | O(log n) | O(log n) | Siempre el max/min |
| BST (manual) | O(h) | O(h) | O(h) | O(h) | h=O(log n) si balanceado |

---

## 7. Proceso de Resolución en Competencias

Basado en Laaksonen (Cap. 1) y Halim et al. (CP4):

1. **Leer el enunciado completo** y entender qué se pide exactamente.
2. **Identificar n** (el tamaño del input) y el límite de tiempo.
3. **Estimar la complejidad necesaria** usando la tabla de la Sección 4.
4. **Elegir la estructura de datos** adecuada al problema.
5. **Diseñar el algoritmo** — la parte más difícil. Generalmente hay un truco o insight clave.
6. **Implementar** — rápido y sin bugs.
7. **Probar con los ejemplos** del enunciado.
8. **Enviar** y analizar el veredicto.

> "Most programming contest problems can be solved using simple and short algorithms, but the difficult part is to invent the algorithm. Competitive programming is not about learning complex and obscure algorithms by heart, but rather about learning problem solving and ways to approach difficult problems using simple tools."
> — Laaksonen, p. 3

---

*Resumen basado en el contenido real de: Laaksonen (Cap. 1, 3, 4, 5), CLRS (Cap. 2, 3, 10, 11, 12, 13), Skiena (Cap. 2), Halim et al. (CP4 — artículo IOI 2020).*
