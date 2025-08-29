#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int dist(const string &a, const string &b){
    int d = 0;
    for (int i = 0; i < 4; ++i) d += (a[i] != b[i]);
    return d;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T, N;

    if(!(cin >> T)) return 0;

    while (T--) {
        int N;
        cin >> N;
        vector<string> m(N);
        for (int i = 0; i < N; ++i) cin >> m[i];

        if (N > 32) {
            cout << 0 << '\n';
            continue;
        }

        int ans = 12; // 최대
        
        for (int i = 0; i < N; ++i) {
            for (int j = i + 1; j < N; ++j) {
                int dij = dist(m[i], m[j]);
                for (int k = j + 1; k < N; ++k) {
                    int d = dij + dist(m[j], m[k]) + dist(m[i], m[k]);
                    ans = min(ans, d);
                    if (ans == 0) break;
                }
                if (ans == 0) break;
            }
            if (ans == 0) break;
        }
        cout << ans << '\n';
    }
    return 0;
}
