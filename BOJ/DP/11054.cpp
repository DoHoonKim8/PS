#include <iostream>

using namespace std;

int main() {
    int N;
    cin >> N;

    int numbers[N + 1];
    for (int i = 1; i <= N; i++) cin >> numbers[i];

    int longest_increasing[N + 1]; // i번째 인덱스를 마지막으로 하는 가장 긴 증가 수열의 길이
    int longest_bytonic[N + 1]; // i번째 인덱스를 마지막으로 하는 가장 긴 바이토닉 수열의 길이

    longest_increasing[1] = 1;
    longest_bytonic[1] = 1;

    for (int i = 2; i <= N; i++) {
        int longest = 0;
        for (int j = i - 1; j >= 1; j--) {
            if (numbers[j] < numbers[i] && longest < longest_increasing[j])
                longest = longest_increasing[j];
        }
        longest_increasing[i] = longest + 1;
    }

    for (int i = 2; i <= N; i++) {
        int longest = 0;
        for (int j = i - 1; j >= 1; j--) {
            if (numbers[j] > numbers[i] && longest < longest_bytonic[j])
                longest = longest_bytonic[j];
            else if (numbers[j] < numbers[i] && longest < longest_increasing[j])
                longest = longest_increasing[j];
        }
        longest_bytonic[i] = longest + 1;
    }

    int result = longest_bytonic[1];
    for (int i = 2; i <= N; i++) {
        if (result < longest_bytonic[i]) result = longest_bytonic[i];
    }

    cout << result << endl;

    return 0;
}
