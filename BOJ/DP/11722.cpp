#include <iostream>
#define MAX 1001

using namespace std;

int numbers[MAX];
int longest[MAX];
 
int main() {
    int N;
    cin >> N;

    for (int i = 1; i <= N; i++) cin >> numbers[i];

    longest[1] = 1;
    for (int i = 2; i <= N; i++) {
        int length = 0;
        for (int j = i - 1; j >= 1; j--) {
            if (numbers[i] < numbers[j] && length < longest[j]) length = longest[j];
        }
        longest[i] = length + 1;
    }

    int result = longest[1];
    for (int i = 2; i <= N; i++) {
        if (result < longest[i]) result = longest[i];
    }

    cout << result << endl;
    return 0;
}
