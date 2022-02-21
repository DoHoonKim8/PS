#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef pair<int, int> INTERVAL;

bool compare(INTERVAL& i1, INTERVAL& i2) {
    int start1 = i1.first;
    int end1 = i1.second;
    int start2 = i2.first;
    int end2 = i2.second;
    return (end1 < end2) || 
        ((end1 == end2) && (start1 < start2));
}

int main() {
    int N;
    cin >> N;

    vector<INTERVAL> intervals;

    for (int i = 0; i < N; i++) {
        int start, end;
        cin >> start >> end;

        intervals.push_back(make_pair(start, end));
    }

    sort(intervals.begin(), intervals.end(), compare);

    int end = 0;
    int count = 0;
    for (int i = 0; i < intervals.size(); i++) {
        if (intervals[i].first >= end) {
            end = intervals[i].second;
            count++;
        }
    }

    cout << count << endl;

    return 0;
}
