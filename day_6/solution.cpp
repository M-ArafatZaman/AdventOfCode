#include <iostream>
#include <fstream>
#include <string>
#include <set>
using namespace std;

string parseInput() {
    ifstream dataFile{"input.in"};
    string data;
    dataFile >> data;
    return data;
}

// Check if characters in a string is unique using set
bool isStrUnique(string s) {
    set<char> a(s.begin(), s.end());
    return a.size() == s.size();
}

int solve(int part=1) {
    const int BUFFER_LEN = part == 1 ? 4 : 14;

    string data = parseInput(); string buffer;
    // Iterate through the buffer stream, and check for a match
    for (int i = 0; i < data.size(); ++i) {
        buffer += data[i];
        if (buffer.size() == BUFFER_LEN && isStrUnique(buffer)) return i+1;

        // Remove chars that exceed the buffer length
        if (buffer.size() >= BUFFER_LEN)
            buffer = buffer.substr(buffer.size()-BUFFER_LEN+1, BUFFER_LEN);
    }

    return -1;
}

int main() {
    cout << "Part 1 => " << solve(1) << endl;
    cout << "Part 2 => " << solve(2) << endl;

    return 0;
}
