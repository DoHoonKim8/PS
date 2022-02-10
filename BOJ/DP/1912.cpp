#include <iostream>

using namespace std;

int main() {
    int N;
    cin >> N;
    int numbers[N + 1];
    for (int i = 1; i <= N; i++) cin >> numbers[i];
    
    int sums[N + 1];
    sums[1] = numbers[1];

    for (int i = 2; i <= N; i++) {
        if (sums[i - 1] < 0) sums[i] = numbers[i];
        else sums[i] = sums[i - 1] + numbers[i]; 
    }    

    int result = sums[1];
    for (int i = 2; i <= N; i++) {
        if (result < sums[i]) result = sums[i];
    }

    cout << result << endl;

    return 0;
}
