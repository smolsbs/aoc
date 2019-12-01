#include <iostream>
#include <fstream>
#include <string>
#include <cmath>

using namespace std;

long fuel(double n){
    return floor(n / 3) - 2;
}

int main(){
    ifstream infile("input");
    string line;
    long p1 = 0, p2 = 0, n, aux;
    
    while ( getline(infile, line)){
        n = atol(line.data());
        p1 += fuel(n);
        aux = fuel(n);
        while (aux > 0){
            p2 += aux;
            aux = fuel(aux);
        }
        
    }
    
    cout << "Part 1: " << p1 << endl;
    cout << "Part 2: " << p2 << endl;
    return 0;
}