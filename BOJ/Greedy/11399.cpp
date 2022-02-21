#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int N;
    vector<int> P;
    
    cin >> N;
    P.resize(N);
    for (int i = 0; i < N; i++) cin >> P[i];

    sort(P.begin(), P.end());

    int result = 0;
    for (int i = 0; i < N; i++) {
        result += (N - i) * P[i];
    }
    cout << result << endl;

    return 0;
}
