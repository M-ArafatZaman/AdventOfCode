#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <stack>
#include <algorithm>
#include <utility>
#include <map>
using namespace std;

// Define types
#define CRATE_TYPE map<int, stack<char>> 
#define INSTRUCTION_TYPE vector<vector<int>>

// Helper functions
template<class T>
void printV(vector<T>& v) {
    cout << "{";
    for (auto a : v) {
        cout << a << ",";
    };
    cout << "}" << endl;
};

template<class T>
void printS(stack<T>& s) {
    vector<T> tmp;
    while(!s.empty()) {
        tmp.insert(tmp.begin(), s.top());
        s.pop();
    }
    cout << "{";
    for (auto i : tmp) {
        cout << i << ",";
        s.push(i);
    };
    cout << "}" << endl;

}

// Parse inputs
pair<CRATE_TYPE, INSTRUCTION_TYPE> parseInput(string fName = "TD.in") {
    CRATE_TYPE crates;
    INSTRUCTION_TYPE instructions;

    // Open file
    ifstream dataFile{fName};

    // Read and parse each line
    while (dataFile) {
        string line;
        getline(dataFile, line);

        if (line[1] == '1') break; // End of crates
        
        for (int c = 0; c < line.length(); ++c) {
            if (line[c] < 'A' || line[c] > 'Z') continue;
            
            int col = ((c-1)/4) + 1;
            
            crates[col].push((char)line[c]);
        };
    }

    // We need to reverse each stack
    for (auto a : crates) {
        vector<char> tmp;
        while(!a.second.empty()) {
            tmp.push_back(a.second.top());
            a.second.pop();
        };
        for (auto i : tmp) {
            a.second.push(i);
        };
        cout << a.first << " = ";
        printS(a.second);
    }

    return {crates, instructions};
};

int main() {
    INSTRUCTION_TYPE s = {
        {1,2,3}
    };

    auto v = parseInput();

    /* stack<int> a;
    a.push(1);
    a.push(2);
    a.push(3);
    a.push(4);

    printS(a);
    printS(a); */

    return 0;
}