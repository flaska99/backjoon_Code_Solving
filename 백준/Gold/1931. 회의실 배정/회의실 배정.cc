#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool cmp_meetroom(pair<int,int> &a, pair<int,int> &b) {
    if (a.second == b.second) return a.first < b.first;
    return a.second < b.second;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    if(!(cin >> N)) return 0;

    vector<pair<int, int>> meet_room(N);

    for (int i = 0; i < N; ++i){
        cin >> meet_room[i].first >> meet_room[i].second;
    }

    sort(meet_room.begin(), meet_room.end(), cmp_meetroom);

    int count = 0;
    int last_end = 0;

    for (auto &[start, end] : meet_room) {
        if (start >= last_end) {
            ++count;
            last_end = end;
        }
    }

    cout << count;
    return 0;
}