#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    int T;
    cin >> T;
    int n;
    int stickers[3][100000];
    int maxSums[3][100000];

    for (int t = 1; t <= T; t++) {
        cin >> n;
        for (int i = 1; i <= n; i++) {
            cin >> stickers[1][i];
        }
        for (int i = 1; i <= n; i++) {
            cin >> stickers[2][i];
        }

        maxSums[1][1] = stickers[1][1];
        maxSums[2][1] = stickers[2][1];
        maxSums[1][2] = stickers[2][1] + stickers[1][2];
        maxSums[2][2] = stickers[1][1] + stickers[2][2];

        for (int i = 3; i <= n; i++) {
            maxSums[1][i] = max(maxSums[2][i - 1], maxSums[2][i - 2]) + stickers[1][i];
            maxSums[2][i] = max(maxSums[1][i - 1], maxSums[1][i - 2]) + stickers[2][i];
        }

        cout << max(maxSums[1][n], maxSums[2][n]) << endl;
    }

    return 0;
}
