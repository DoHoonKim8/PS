#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

vector<string> answer;
vector<vector<string>> ticketsv;
map<pair<string, string>, bool> visited;

void solve
    (vector<vector<string>>& used_tickets) {
    
    // 항공권을 모두 사용하면 종료한다
    if (ticketsv.size() == 0) return;
    
    // 아직 항공권이 남아 있는데 이용할 수 있는 항공권이 없으면 dfs가 실패한 것이므로 종료한다
    string src = answer.back();
    auto it = find_if(ticketsv.begin(), ticketsv.end(), [src](vector<string>& t) {
        return !src.compare(t[0]);
    });
    if (it == ticketsv.end()) return;

    for (auto it = ticketsv.begin(); it != ticketsv.end(); it++) {
        if (!src.compare((*it)[0])) {
            answer.push_back((*it)[1]);
            used_tickets.push_back(*it);
            auto it_next = ticketsv.erase(it);
            solve(used_tickets);
            if (ticketsv.size() == 0) return;
            answer.pop_back();
            ticketsv.insert(it_next, used_tickets.back());
            used_tickets.pop_back();
        }
    }
}

bool compare(vector<string>& v1, vector<string>& v2) {
    return (v1[0] < v2[0]) || (v1[0] == v2[0] && v1[1] < v2[1]);
}

vector<string> solution(vector<vector<string>> tickets) {
    vector<vector<string>> used_tickets;
    ticketsv.insert(ticketsv.begin(), tickets.begin(), tickets.end());

    sort(ticketsv.begin(), ticketsv.end(), compare);
    answer.push_back("ICN");

    solve(used_tickets);

    return answer;
}

int main() {
    vector<string> answer = solution({ {"ICN", "SFO"}, {"ICN", "ATL"}, {"SFO", "ATL"}, {"ATL", "ICN"}, {"ATL","SFO"} });

    for (string& s: answer) cout << s << endl;

    return 0;
}
