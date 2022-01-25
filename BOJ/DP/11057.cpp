#include <iostream>

#define MOD 10007

using namespace std;

int main() {
    int N;
    cin >> N;

    int numbers[N + 1][10];

    for (int i = 0; i <= 9; i++) {
        numbers[1][i] = 1;
    }

    for (int len = 2; len <= N; len++) {
        numbers[len][0] = 1;
        for (int j = 1; j <= 9; j++) {
            numbers[len][j] = (numbers[len][j - 1] + numbers[len - 1][j]) % MOD;
        }
    }
    int result = 0;
    for (int i = 0; i <= 9; i++) {
        result += numbers[N][i];
    }
    cout << result % MOD;
    return 0;
}