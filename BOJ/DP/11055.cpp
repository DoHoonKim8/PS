#include <iostream>

using namespace std;

int main() {
    int N;
    cin >> N;
    int numbers[N + 1];
    int biggest[N + 1];


    for (int i = 1; i <= N; i++) cin >> numbers[i];

    biggest[1] = numbers[1];

    for (int i = 2; i <= N; i++) {
        int sum = 0;
        for (int j = i - 1; j >= 1; j--) {
            if (numbers[j] < numbers[i] && sum < biggest[j]) sum = biggest[j];
        }
        biggest[i] = sum + numbers[i];
    }

    int result = biggest[1];
    for (int i = 2; i <= N; i++) {
        if (result < biggest[i]) result = biggest[i];
    }

    cout << result << endl;

    return 0;
}
