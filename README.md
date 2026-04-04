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
g++ -std=c++11 -O2 -Wall -Wextra -Wshadow -o sol sol.cpp
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

## Setup en Mac

### 1. Instalar g++
Mac no trae g++ por defecto. Instalá las herramientas de desarrollo de Xcode:
```bash
xcode-select --install
```
Verificá que quedó instalado:
```bash
g++ --version
```

### 2. Instalar VSCode
Descargalo desde https://code.visualstudio.com/ e instalá la extensión **C/C++** de Microsoft.

### 3. Abrir el repo
```bash
cd ~/Desktop/Universidad/algoritmos-unq
code .
```

### Compilar un programa (Mac)
```bash
g++-15 -std=c++11 -O2 -Wall -Wextra -Werror -Wpedantic -Wshadow -Wconversion -o sol sol.cpp
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

> **Nota:** En Mac, `g++` es en realidad Clang bajo el capó. Para usar GCC real (más fiel al juez online) podés instalarlo con `brew install gcc` y usar `g++-15` en lugar de `g++`.

---

## Debuggear con VS Code (Mac)

### 1. Instalar la extensión
Instalá **C/C++** de Microsoft (ms-vscode.cpptools) desde el panel de extensiones.

### 2. Compilar con símbolos de debug
```bash
g++-15 -std=c++11 -g -o sol sol.cpp
```

### 3. Configurar launch.json
Creá `.vscode/launch.json` con:
```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Debug C++",
      "type": "cppdbg",
      "request": "launch",
      "program": "${workspaceFolder}/sol",
      "args": [],
      "stopAtEntry": false,
      "cwd": "${workspaceFolder}",
      "MIMode": "lldb"
    }
  ]
}
```

### 4. Atajos del debugger
| Acción | Atajo |
|--------|-------|
| Poner/sacar breakpoint | `F9` |
| Iniciar debug | `F5` |
| Siguiente línea (step over) | `F10` |
| Entrar a función (step into) | `F11` |
| Salir de función | `Shift+F11` |
| Continuar hasta próximo breakpoint | `F5` |

### Configuración actual de VS Code
- Compilador: `g++-15`
- Standard: `c++11`
- Archivo de config: `.vscode/c_cpp_properties.json`

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