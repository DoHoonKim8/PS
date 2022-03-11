#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool compare(pair<int, int> p1, pair<int, int> p2) {
    return p1.first < p2.first ||
        (p1.first == p2.first) && (p1.second > p2.second);
}

vector<int> solution(vector<int> answers) {
    vector<int> answer;
    int correctOne = 0;
    int correctTwo = 0;
    int correctThree = 0;
    for (int i = 0; i < answers.size(); i++) {
        if ((i + 1) % 5 == answers[i]) correctOne++;
    }
    
    for (int i = 0; i < answers.size(); i++) {
        if (i % 2 == 0 && answers[i] == 2) correctTwo++;
     	if (i % 8 == 1 && answers[i] == 1) correctTwo++;
        if (i % 8 == 3 && answers[i] == 3) correctTwo++;
        if (i % 8 == 5 && answers[i] == 4) correctTwo++;
        if (i % 8 == 7 && answers[i] == 5) correctTwo++;
    }
    
    for (int i = 0; i < answers.size(); i++) {
        if ((i / 2) % 10 == 0 && answers[i] == 3) correctThree++;
        if ((i / 2) % 10 == 1 && answers[i] == 1) correctThree++;
        if ((i / 2) % 10 == 2 && answers[i] == 2) correctThree++;
        if ((i / 2) % 10 == 3 && answers[i] == 4) correctThree++;
        if ((i / 2) % 10 == 4 && answers[i] == 5) correctThree++;
    }
    
    vector<pair<int, int>> corrects =
        { make_pair(correctOne, 1), make_pair(correctTwo, 2), make_pair(correctThree, 3) };
    sort(corrects.begin(), corrects.end(), compare);
    
    answer.push_back(corrects[2].second);
    if (corrects[1].first == corrects[2].first) answer.push_back(corrects[1].second);
    if (corrects[0].first == corrects[2].first) answer.push_back(corrects[0].second);
    
    return answer;
}