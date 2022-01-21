#include <iostream>

using namespace std;

static int* counts;

int getCount(int n) {
    if (n == 0) return 0;
    if (n == 1) {
        counts[0] = 1;
        return 1;
    }
    if (n == 2) {
        counts[1] = 2;
        return 2;
    }
    if (!counts[n - 1]) counts[n - 1] = (getCount(n - 1) + getCount(n - 2)) % 10007;
    return counts[n - 1];
}

int main() {
    int n;
    cin >> n;

    counts = new int[n];
    
    cout << getCount(n) << endl;
}