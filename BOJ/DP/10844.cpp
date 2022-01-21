#include <iostream>
#define MOD 1000000000

using namespace std;

int main() {
    int N;
    cin >> N;

    long long** endWithNum = new long long*[N]; // 길이가 N이고, 특정 숫자로 끝나는 계단수의 개수를 저장

    for (int i = 0; i < N; i++) {
        if (i == 0) {
            endWithNum[0] = new long long [10]{ 0, 1, 1, 1, 1, 1, 1, 1, 1, 1 };
        } else {
            endWithNum[i] = new long long [10]{ 0 };
        }
    }

    long long result = 0;
    for (int i = 1; i < N; i++) {
        endWithNum[i][0] = endWithNum[i - 1][1] % MOD;
        endWithNum[i][9] = endWithNum[i - 1][8] % MOD;
        for (int j = 1; j <= 8; j++)
            endWithNum[i][j] = (endWithNum[i - 1][j - 1] + endWithNum[i - 1][j + 1]) % MOD;
    }
    for (int i = 0; i < 10; i++) {
        result += endWithNum[N - 1][i];
    }
    cout << result % MOD << endl;

    for (int i = 0; i < N; i++) {
        delete[] endWithNum[i];
    }
    delete[] endWithNum;
}