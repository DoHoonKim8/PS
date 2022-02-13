#include <iostream>

using namespace std;

int main() {
    int N, M;
    cin >> N >> M;

    int result;
    if (N == 1) result = 1;
    else if (N == 2 && M <= 8) result = 1 + (M - 1) / 2;
    else if (N == 2 && M > 8) result = 4;
    else if (M < 5) result = M;
    else if (M == 5 || M == 6) result = 4;
    else if (M == 7) result = 5;
    else result = M - 2;

    cout << result << endl;
    return 0;
}
