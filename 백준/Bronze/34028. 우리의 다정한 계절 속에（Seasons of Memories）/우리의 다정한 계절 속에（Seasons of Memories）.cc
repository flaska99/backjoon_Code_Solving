#include <iostream>
#include <string>

using namespace std;

int get_season(int m) {
    if (3 <= m && m <= 5) return 0;  // 봄
    else if (6 <= m && m <= 8) return 1;  // 여름
    else if (9 <= m && m <= 11) return 2; // 가을
    else return 3;                        // 겨울
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int year, month, day;
    cin >> year >> month >> day;

    int debut_year = 2014, debut_season = 3;

    int cur_year = year;
    int cur_season = get_season(month);
    if (cur_season == 3 && month <= 2) cur_year--; 

    int answer = (cur_year - debut_year) * 4 + (cur_season - debut_season) + 1;

    cout << answer;
    return 0;
}