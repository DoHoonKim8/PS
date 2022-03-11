#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> citations) {
    int answer = 0;

    sort(citations.rbegin(), citations.rend());

    for (int i = 0; i < citations.size(); i++) {
        if (i + 1 > citations[i]) break;
        answer++;
    }

    return answer;
}

int main() {
    int answer = solution({ 4, 4, 4, 4, 5 });
    cout << answer << endl;
    return 0;
}
