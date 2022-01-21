#include <iostream>

using namespace std;

int main() {
    int cases;
    cin >> cases;
    int num;
    int* counts = new int[11];
    counts[0] = 1;
    counts[1] = 2;
    counts[2] = 4;

    for (int i = 0; i < cases; i++) {
        cin >> num;
        if (!counts[num]) {
            for (int j = 3; j < num; j++) {
                counts[j] = counts[j - 1] + counts[j - 2] + counts[j - 3];
            }
        }
        cout << counts[num - 1] << endl;
    }
}
