#include <iostream>
#include <string.h>
#include <algorithm>
#define MAX 100000

using namespace std;

int main() {
    char N[MAX];
    cin >> N;

    int len = strlen(N);
    sort(N, N + len, greater<char>());

    int mod = 0;
    for (int i = 0; i < len; i++) {
        mod += (N[i] - '0');
    }
    if (mod % 3 == 0 && N[len - 1] == '0') cout << N << endl; 
    else cout << -1 << endl;

    return 0;
}
