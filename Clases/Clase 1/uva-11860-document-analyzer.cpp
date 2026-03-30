/**
 * Author: Francisco Soulignac
 * Time in UVA: 0.63s
 *
 * Input: un string s formado por palabras, donde una palabra es una secuencia
 * consecutiva de letras minusculas
 * Output: los indices p y q tal que todas las palabras del documento aparecen
 * entre la p-esima y la q-esima palabras (inclusive), minimizando q-p y luego p
 * Restricciones: 10^6 palabras en total en todo el input (no dice cuántas no palabras)
 *
 * Solucion: primero creamos una secuencia de numeros donde cada numero representa una palabra
 * Despues buscamos el intervalo [p, q] que contiene todos los numeros minimizando p-q y luego p.
 * Para ello, movemos primero q hasta cubrir todos los numeros, luego movemos p manteniendo todas
 * los numeros y evaluamos q-p.
 * Complejidad esperada: O(|s|)
 * Dificultad: 3 (tiene un sliding window y hay que mantener bien los strings)
 */

#include <iostream>
#include <sstream>
#include <unordered_map>
#include <vector>

using namespace std;

int main() {
 
    int T,k; cin >> T;
    
    while(k++ < T) {
        string next;
        unordered_map<string, int> to_int;
        vector<int> doc;
        
        while(cin >> next, next[0] != 'E'){
            for(auto& c : next) if('a' > c or 'z' < c) c = ' ';
            stringstream split(next);        
            
            string word;
            while(split >> word) {
                auto pos = to_int.find(word);
                if(pos == to_int.end()) {
                    pos = to_int.insert({word, to_int.size()}).first;
                }
                doc.push_back(pos->second);
            }
        }
        
        vector<int> count(to_int.size(), 0);
        int p = 0, q = -1, zero = count.size(), res_p = 0, res_q = doc.size()-1;
        while(true) {
            while(zero > 0 and ++q < doc.size()) if(++count[doc[q]] == 1) zero--;
            if(zero > 0) break;    
            
            while(count[doc[p]] > 1) count[doc[p++]] -= 1;
    
            if(q - p < res_q - res_p) {res_p = p; res_q = q;}
            count[doc[p++]] -= 1;
            
            zero = 1;
        }
        cout << "Document " << k << ": " << res_p+1 << " " << res_q+1 << '\n';
    }
    
    return 0;
}
