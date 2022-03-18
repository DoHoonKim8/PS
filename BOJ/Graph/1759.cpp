#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

int L, C;
vector<char> characters;
string current;

bool isValid(string& s) {
    int mNum = 0;
    int jNum = 0;

    for (int i = 0; i < s.length(); i++) {
        if (s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' || s[i] == 'u') {
            mNum++;
        } else jNum++;
    }

    return (s.length() == L) && (mNum >= 1) && (jNum >= 2);
}

void dfs(int index) {
    if (isValid(current)) {
        cout << current << endl;
        return;
    }

    if (index == C) return;

    current.push_back(characters[index]);
    dfs(index + 1);
    current.pop_back();

    dfs(index + 1);
}

int main() {
    cin >> L >> C;

    characters.resize(C);

    for (int i = 0; i < C; i++) cin >> characters[i];

    sort(characters.begin(), characters.end());

    dfs(0);

    return 0;
}
