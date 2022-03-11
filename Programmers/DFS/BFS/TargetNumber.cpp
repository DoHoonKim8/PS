#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int answer = 0;
vector<int> visited;

void dfs(vector<int>& numbers, int target, int index, int sum) {
    if (index == numbers.size()) {
        if (sum == target) answer++;
        return;
    }

    dfs(numbers, target, index + 1, sum + numbers[index]);
    dfs(numbers, target, index + 1, sum - numbers[index]);
}

int solution(vector<int> numbers, int target) {
    int sum = 0;
    visited.resize(numbers.size());
    fill(visited.begin(), visited.end(), false);

    dfs(numbers, target, 0, 0);    
    return answer;
}

int main() {
    int answer = solution({ 1, 1, 1, 1, 1 }, 3);
    cout << answer << endl;
    return 0;
}
