#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>

using namespace std;

vector<int> split(string strToSplit, char delimeter){
    stringstream ss(strToSplit);
    string item;
    vector<int> splittedStrings;
    while (getline(ss, item, delimeter))
    {
       splittedStrings.push_back( atoi(item.c_str()));
    }
    return splittedStrings;
}

long machine(vector<int> code, int arg1, int arg2){
    code[1] = arg1;
    code[2] = arg2;

    int ip = 0, pA, pB, rA, opcode;

    while(1){
        opcode = code[ip];
        if (opcode == 99){break;}
        pA = code[ip+1];
        pB = code[ip+2];
        rA = code[ip+3];

        if (opcode == 1){
            code[rA] = code[pA] + code[pB];
        }else if(opcode == 2){
            code[rA] = code[pA] * code[pB];
        }
        ip += 4;
    }
    return code[0]; 
}


int main(){
    ifstream infile("input");
    string line;
    getline(infile, line); 
    vector<int> data = split(line, ',');

    cout << machine(data, 12, 2) << endl;

    for (int i = 0; i < 100; i++){
        for(int j = 0; j < 100; j++){
            if (machine(data, i, j) == 19690720){
                cout << 100*i+j << endl;
            }
        }
    }
    return 0;
}