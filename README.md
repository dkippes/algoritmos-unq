# Algoritmos UNQ

Repositorio de ejercicios de la materia Algoritmos (UNQ).

## Setup inicial (solo la primera vez)

### 1. Instalar WSL2 + Ubuntu
Desde PowerShell como administrador:
```powershell
wsl --install -d Ubuntu
```
Reiniciar Windows y configurar usuario/contraseña de Ubuntu.

### 2. Instalar g++
Desde la terminal de Ubuntu:
```bash
sudo apt update && sudo apt install g++ -y
```

### 3. Instalar VSCode en Windows
Descargar desde https://code.visualstudio.com/. La extensión WSL se instala sola la primera vez que hacés `code .` desde Ubuntu.

---

## Uso diario

### Abrir el entorno
1. Abrir Ubuntu desde el menú inicio.
2. Navegar a la carpeta del repo:
```bash
cd /mnt/c/Users/kippe/Desktop/Universidad/algoritmos-unq
```
3. Abrir VSCode:
```bash
code .
```

### Compilar un programa
```bash
g++ -std=c++17 -O2 -Wall -Wextra -Wshadow -o sol sol.cpp
```

### Ejecutar
```bash
./sol
```

### Ejecutar con input desde consola
```bash
echo "5 3" | ./sol
```

### Ejecutar con input desde archivo
```bash
cat in.txt | ./sol
```

### Ejecutar y guardar output en archivo
```bash
cat in.txt | ./sol > out.txt
```

---

## Template base para cada problema

```cpp
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    // tu código acá

    return 0;
}
```