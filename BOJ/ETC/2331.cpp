#include <iostream>
#include <vector>
#include <math.h>

using namespace std;

vector<int> sequence;

int next(int N, int P) {
    int dividend = N;
    int result = 0;
    for (int i = 1; ; i++) {
        result += pow(dividend % 10, P);
        dividend = dividend / 10;
        if (dividend == 0) break;
    }
    return result;
}

int contains(int elem) {
    for (int i = 0; i < sequence.size(); i++) {
        if (sequence[i] == elem) return i;
    }
    return -1;
}

int main() {
    int A, P;
    cin >> A >> P;

    int elem = A;
    int idx;
    while (1) {
        idx = contains(elem);
        if (idx != -1) break;
        sequence.push_back(elem);
        elem = next(elem, P);
    }

    cout << idx << endl;
    return 0;
}
