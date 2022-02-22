#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int N;
    vector<int> seq;

    cin >> N;
    seq.resize(N);
    for (int i = 0; i < N; i++) cin >> seq[i];

    vector<int> pos;
    vector<int> neg;

    for (int i = 0; i < N; i++) {
        if (seq[i] > 0) pos.push_back(seq[i]);
        else neg.push_back(seq[i]);
    }

    sort(pos.rbegin(), pos.rend());
    sort(neg.begin(), neg.end());

    int result = 0;
    for (int i = 0; i < pos.size();) {
        if (i < pos.size() - 1 && pos[i] != 1 && pos[i + 1] != 1) {
            result += pos[i] * pos[i + 1];
            i += 2;
        } else {
            result += pos[i];
            i++;
        }
    }

    for (int i = 0; i < neg.size();) {
        if (i == neg.size() - 1) {
            result += neg[i];
            i++;
        } else {
            result += neg[i] * neg[i + 1];
            i += 2;
        }
    }

    cout << result << endl;

    return 0;
}
