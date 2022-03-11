#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

vector<int> solution(vector<string> genres, vector<int> plays) {
    vector<int> answer;
    map<string, vector<int>> playlists;
    map<int, vector<int>> playlists2;

    for (int i = 0; i < genres.size(); i++)
        playlists[genres[i]].push_back(i);
    
    for (auto& [genre, musics]: playlists) {
        int totalPlays = 0;
        for (int music: musics) {
            totalPlays += plays[music];
        }
        sort(musics.begin(), musics.end(), [plays](int i, int j) -> bool { return plays[i] > plays[j]; });
        playlists2[totalPlays] = musics;
    }

    for (auto it = playlists2.rbegin(); it != playlists2.rend(); it++) {
        if ((it->second).size() >= 2) {
            answer.push_back((it -> second)[0]);
            answer.push_back((it -> second)[1]);
        } else
            answer.push_back((it -> second)[0]);
    }

    return answer;
}

int main() {
    vector<string> genres = { "classic", "pop", "classic", "classic", "pop" };
    vector<int> plays = { 500, 600, 150, 800, 2500 };
    vector<int> answer = solution(genres, plays);

    for (int i = 0; i < answer.size(); i++) cout << answer[i] << endl;

    return 0;
}
