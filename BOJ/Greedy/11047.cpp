#include <iostream>

using namespace std;

int main() {
    int N, K;

    cin >> N >> K;
    int numbers[N + 1];

    for (int i = 1; i <= N; i++) cin >> numbers[i];
    int result = 0;
    for (int i = N; i >= 1; i--) {
        if (K == 0) break;
        if (numbers[i] <= K) {
            result += K / numbers[i];
            K = K % numbers[i];
        }
    }

    cout << result << endl;
    return 0;
}
