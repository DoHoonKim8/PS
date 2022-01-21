#include <iostream>

using namespace std;

static int* counts;

int main() {
    int n;
    cin >> n;

    counts = new int[n];
    counts[0] = 1;
    counts[1] = 3;
    for (int i = 2; i < n; i++) {
        counts[i] = (counts[i - 1] + 2 * counts[i - 2]) % 10007;
    }
    
    cout << counts[n - 1] << endl;
}