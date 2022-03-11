#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <unordered_map>

using namespace std;

int answer = 0;
unordered_map<string, bool> visited;
unordered_map<string, vector<string>> adjs;

bool isAdjacentWords(string& s1, string& s2) {
    int len = s1.length();
    int differs = 0;

    for (int i = 0; i < len; i++) {
        if (s1[i] != s2[i]) differs++;
    }
    return (differs == 1);
}

int bfs(string begin, string target, vector<string> words) {
    queue<string> q;
    for (string& s: words) {
        if (isAdjacentWords(begin, s)) {
            visited[s] = true;
            q.push(s);
        }
    }

    int count = 1;
    int elems = q.size();
    while (!q.empty()) {
        if (elems == 0) {
            elems = q.size();
            count++;
        }
        string front = q.front();
        if (!front.compare(target)) break;
        for (string& s: adjs[front]) {
            if (!visited[s]) {
                visited[s] = true;
                q.push(s);
            }
        }
        q.pop();
        elems--;
    }
    return count;
}

int solution(string begin, string target, vector<string> words) {
    bool exists = false;
    for (int i = 0; i < words.size(); i++) {
        if (!words[i].compare(target)) exists = true;
    }

    if (!exists) return 0;

    for (int i = 0; i < words.size(); i++) {
        for (int j = i + 1; j < words.size(); j++) {
            if (isAdjacentWords(words[i], words[j])) {
                adjs[words[i]].push_back(words[j]);
                adjs[words[j]].push_back(words[i]);      
            }
        }
    }

    answer = bfs(begin, target, words);

    return answer;
}

int main() {
    int answer = solution("hit", "cog", { "hot", "dot", "dog", "lot", "log" });

    cout << answer << endl;
    return 0;
}
