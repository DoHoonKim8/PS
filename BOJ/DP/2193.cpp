#include <iostream>

using namespace std;

int main() {
    int N;
    
    cin >> N;

    long numbers[N][2];

    numbers[1][0] = 0;
    numbers[1][1] = 1;

    for (int i = 2; i <= N; i++) {
        numbers[i][0] = numbers[i - 1][0] + numbers[i - 1][1];
        numbers[i][1] = numbers[i - 1][0];
    }

    cout << numbers[N][0] + numbers[N][1];
    return 0;
}