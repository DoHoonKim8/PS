#include <iostream>
#include <string.h>
#define MAX 1000000

using namespace std;

char enigma[5001];
int dp[5001] = { 0 };

int main() {
    cin >> enigma;
    int len = strlen(enigma);

    dp[0] = 1;
    for (int i = 1; i <= len; i++) {
        if (enigma[i - 1] > '0' && enigma[i - 1] <= '9') dp[i] += dp[i - 1];
        if (i >= 2 &&
            enigma[i - 2] == '1' || 
            enigma[i - 2] == '2' && enigma[i - 1] >= '0' && enigma[i - 1] <= '6')
                dp[i] += dp[i - 2];
    }

    cout << dp[len] << endl;
    return 0;
}
