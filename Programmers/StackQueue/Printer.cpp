#include <iostream>
#include <string>
#include <vector>

using namespace std;

int solution(vector<int> priorities, int location) {
    int answer = 0;
    vector<pair<int, int>> prints;

    for (int i = 0; i < priorities.size(); i++) {
        prints.push_back(make_pair(i, priorities[i]));
    }

    int count = 0;
    while (1) {
        int max_priority = prints[0].second;
        int idx = 0;
        for (int j = 1; j < prints.size(); j++) {
            if (prints[j].second > max_priority) {
                max_priority = prints[j].second;
                idx = j;
            }
        }
        if (prints[idx].first == location) {
            answer = count;
            break;
        }
        if (idx != 0) {
            prints.push_back(prints.front());
            prints.begin()++;
        }
        prints.erase(next(prints.begin(), idx));
    }

    return answer;
}

int main() {
    int answer = solution({ 1, 1, 9, 1, 1, 1 }, 0);
    cout << answer << endl;
    return 0;
}
