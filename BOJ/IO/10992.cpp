#include <iostream>

using namespace std;

int main () {
    int N;
    cin >> N;
    int col = 2 * N - 1;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < col; j++) {
            if (i == N - 1) cout << '*';
            else if (j == (N - 1) - i || j == (N - 1) + i) cout << '*';
            else cout << ' ';
        }
        cout << endl;
    }
    cout << endl;
    return 0;
}
