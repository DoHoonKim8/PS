#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    int N;
    cin >> N;
    int numbers[N + 1];
    int longest[N + 1]; // i(1 <= i <= N)번째 원소를 마지막으로 하는 가장 긴 증가 수열의 길이

    for (int i = 1; i <= N; i++) cin >> numbers[i];

    longest[1] = 1;

    for (int i = 2; i <= N; i++) {
        int biggest = 0;
        for (int j = i - 1; j >= 1; j--) {
            if (numbers[j] < numbers[i] && biggest < longest[j]) {
                biggest = longest[j];
            }
        }
        longest[i] = biggest + 1;
    }

    int result = longest[1];

    for (int i = 2; i <= N; i++) {
        if (result < longest[i]) result = longest[i];
    }

    cout << result << endl;

    return 0;
}