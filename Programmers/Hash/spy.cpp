#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

int solution(vector<vector<string>> clothes) {
    int answer = 0;
    unordered_map<string, int> hashMap;
    vector<string> keys;

    for (int i = 0; i < clothes.size(); i++) {
        string key = clothes[i][1];
        if (!hashMap[key]) keys.push_back(key);
        hashMap[key]++;
    }

    int times = 1;
    for (int i = 0; i < keys.size(); i++) {
        times *= (hashMap[keys[i]] + 1);
    }

    answer = times - 1;

    return answer;
}