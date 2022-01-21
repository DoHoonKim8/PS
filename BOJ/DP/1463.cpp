#include <iostream>
#include <algorithm>

using namespace std;

static int* minCalculateCounts;

int getMinCalculateCount(int n) {
    if (n == 1) return 0;
    if (n == 2) {
        minCalculateCounts[1] = 1;
        return 1;
    }
    if (minCalculateCounts[n - 1]) return minCalculateCounts[n - 1];
    if (n % 2 == 0 && n % 3 != 0)
        minCalculateCounts[n - 1] =
            min({ getMinCalculateCount(n - 1), getMinCalculateCount(n / 2) }) + 1; 
    else if (n % 2 != 0 && n % 3 == 0)
        minCalculateCounts[n - 1] =
            min({ getMinCalculateCount(n - 1), getMinCalculateCount(n / 3) }) + 1;
    else if (n % 2 != 0 && n % 3 != 0)
        minCalculateCounts[n - 1] = getMinCalculateCount(n - 1) + 1;
    else
        minCalculateCounts[n - 1] =
            min({ getMinCalculateCount(n - 1),
                getMinCalculateCount(n / 2),
                getMinCalculateCount(n / 3) }) + 1;
    return minCalculateCounts[n - 1];
}

int main() {
    int N;
    cin >> N;
    minCalculateCounts = new int[N];
    cout << getMinCalculateCount(N) << endl;
    return 0;
}