#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool compare(const int a, const int b) {
    string a_string = to_string(a);
    string b_string = to_string(b);
    return a_string.append(b_string) > b_string.append(a_string);
}

string solution(vector<int> numbers) {
    string answer = "";

    sort(numbers.begin(), numbers.end(), compare);

    for (int i = 0; i < numbers.size(); i++) {
        answer.append(to_string(numbers[i]));
    }
    
    if (!answer.compare(string(answer.length(), '0')))
        answer = "0";
    return answer;
}

int main() {
    string answer = solution({ 0, 0, 0 });
    cout << answer << endl;
    return 0;
}
