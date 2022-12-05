#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <stack>
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
pair<CRATE_TYPE, INSTRUCTION_TYPE> parseInput(string fName = "data.in") {
    CRATE_TYPE crates;
    INSTRUCTION_TYPE instructions;

    // Open file
    ifstream dataFile{fName};

    string line;
    // Read and parse each line
    while (dataFile) {
        getline(dataFile, line);

        if (line[1] == '1') break; // End of crates
        
        for (int c = 0; c < line.length(); ++c) {
            if (line[c] < 'A' || line[c] > 'Z') continue;
            
            int col = ((c-1)/4) + 1;
            
            crates[col].push((char)line[c]);
        };
    }

    // We need to reverse each stack
    for (auto &a : crates) {
        vector<char> tmp;
        while(!a.second.empty()) {
            tmp.push_back(a.second.top());
            a.second.pop();
        };
        for (auto i : tmp) {
            a.second.push(i);
        };
    }

    // Get instructions
    while (!dataFile.eof()) {
        getline(dataFile, line);
        if (line == "") continue;

        // Parse only numbers
        stringstream ss(line);
        string tmp;
        vector<int> inst;
        int n;
        while (ss >> tmp) {
            try {
                n = stoi(tmp);
            } catch (...) {
                continue;
            };
            inst.push_back(n);
        };
        // Load instructions
        instructions.push_back(inst);
    }

    return {crates, instructions};
};

void part1() {
    auto v = parseInput();
    CRATE_TYPE crates = v.first;
    INSTRUCTION_TYPE instructions = v.second;


    // Go through each instructions
    for (auto i : instructions) {
        int no = i[0], frm = i[1], to = i[2];

        for (int _ = 0; _ < no; ++_) {
            char tmp = crates[frm].top();
            crates[frm].pop();
            crates[to].push(tmp);
        }
    };

    string ans;

    for (auto x: crates) {
        ans += x.second.top();
    }

    cout << "Part1 = " << ans << endl;
}

int main() {
    part1();
    


    return 0;
}