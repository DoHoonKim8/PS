#include <iostream>
#include <math.h>
#define MAX 2187

using namespace std;

int square[MAX + 1][MAX + 1];
int results[3] = { 0 };

void solve(int x, int y, int N) {
    int elem = square[x][y];
    bool isSame = true;
    for (int i = x; i < x + N; i++) {
        for (int j = y; j < y + N; j++) {
            if (square[i][j] != elem) isSame = false;
        }
    }
    if (isSame) {
        results[elem + 1] += 1;
        return;
    }
    for (int xx = x; xx < x + N; xx += N / 3) {
        for (int yy = y; yy < y + N; yy += N / 3) solve(xx, yy, N / 3);
    }
}

int main() {
    int N;
    cin >> N;

    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= N; j++) cin >> square[i][j];
    }

    solve(1, 1, N);
    cout << results[0] << endl;
    cout << results[1] << endl;
    cout << results[2] << endl;
    return 0;
}
