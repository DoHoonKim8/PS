#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int N, M;
    cin >> N >> M;

    vector<int> A, B;
    A.resize(N);
    B.resize(M);

    for (int i = 0; i < N; i++) cin >> A[i];
    for (int i = 0; i < M; i++) cin >> B[i];

    vector<int>::iterator it_A = A.begin ();
    vector<int>::iterator it_B = B.begin ();

    while (it_A != A.end() && it_B != B.end()) {
        if (*it_A < *it_B) {
            cout << *it_A << ' ';
            it_A++;
        }
        else {
            cout << *it_B << ' ';
            it_B++;
        }
    }
    
    while (it_A != A.end()) {
        cout << *it_A << ' ';
        it_A++;
    }
    
    while (it_B != B.end()) {
        cout << *it_B << ' ';
        it_B++;
    }

    return 0;
}
