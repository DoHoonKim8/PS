#include <iostream>
#include <string>
#include <vector>
#include <deque>
#include <math.h>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    deque<int> remaining;

    for (int i = 0; i < progresses.size(); i++) {
        remaining.push_back(ceil((double)(100 - progresses[i]) / speeds[i]));
    }

    auto front = remaining.begin();
    while(front != remaining.end()) {
        int count = 1;
        auto end = front + 1;
        for ( ; end != remaining.end(); end++) {
            if (*end > *front) break;
            count++;
        }
        answer.push_back(count);
        front = end;
    }

    return answer;
}

int main() {
    vector<int> answer = solution({ 93, 30, 55 }, { 1, 30, 5 });
    for (int i = 0; i < answer.size(); i++) cout << answer[i] << ' ';
    return 0;
}
