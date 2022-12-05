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

void solve(int part=1) {
    auto v = parseInput();
    CRATE_TYPE crates = v.first;
    INSTRUCTION_TYPE instructions = v.second;


    // Go through each instructions
    for (auto i : instructions) {
        int no = i[0], frm = i[1], to = i[2];

        // Solve for each parts
        if (part == 1) {
            for (int _ = 0; _ < no; ++_) {
                char tmp = crates[frm].top();
                crates[frm].pop();
                crates[to].push(tmp);
            }
        } else if (part == 2) {
            vector<char> tmpList;
            for (int _ = 0; _ < no; ++_) {
                char tmp = crates[frm].top();
                crates[frm].pop();
                tmpList.insert(tmpList.begin(), tmp);
            }
            for (int crt : tmpList) {
                crates[to].push(crt);
            }
        }
    };

    string ans;

    for (auto x: crates) {
        ans += x.second.top();
    }

    cout << "Part " << part << " = " << ans << endl;
}

int main() {
    solve(1);
    solve(2);

    return 0;
}