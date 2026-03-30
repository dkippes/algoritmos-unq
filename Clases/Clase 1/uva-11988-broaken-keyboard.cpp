/**
 * Author: Francisco Soulignac
 * Time in UVA: 0.22
 *
 * Input: un string s
 * Output: un nuevo string t_n generado secuencialmente a partir de un string inicial t_0
 * y un cursor c.
 * Si s_i es '[' se setea c = 0, si s_i = ']' se setea c = |t_i| y si s_i \not\in {'[',']'},
 * entonces t_i = t_{i-1}[:c] + s_i + t_{i-1}[c:].
 *
 * Solución: emular lo que se pide usando una lista para poder insertar en O(1) en las
 * posiciones intermedias
 * Complejidad: O(|s|)
 * Dificultad: 2 (la solucion mas simple es con una lista que puede ser complejo en Python.  Se puede hacer con una secuencia de indices directamente sobre el input)
 */

#include <iostream>
#include <list>
#include <string>
#include <sstream>

using namespace std;

int main() {

    char c;
    list<char> beiji;
    list<char>::iterator pos;
    string line;
    
    while(getline(cin, line)) {
        istringstream stream(line);
        beiji.clear();
        pos = beiji.end();
        
        while(stream >> c) {
            switch(c) {
                case ']':
                    pos = beiji.end();
                    break;
                case '[':
                    pos = beiji.begin();
                    break;
                default:
                    beiji.insert(pos, c); 
                    break;
            }
        }
        for(auto c : beiji) cout << c;
        cout << '\n'';
    }

    return 0;
}
