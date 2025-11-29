#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int M, N, K;
int board[100][100];
bool visited[100][100];

int dy[4] = { 1, -1, 0, 0 };
int dx[4] = { 0, 0, 1, -1 };

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	

	cin >> M >> N >> K;

	for (int i = 0; i < K; i++) {
		// 직사각형 좌표 받기
		int x1, y1, x2, y2;
		cin >> x1 >> y1 >> x2 >> y2; 

		// 직사각형 좌표 칠하기
		for (int y = y1; y < y2; y++) {
			for (int x = x1; x < x2; x++) {
				board[y][x] = 1;
			}
		}
	}

	vector<int> areas;

	for (int y = 0; y < M; y++) {
		for (int x = 0; x < N; x++) {
			if (board[y][x] == 0 && !visited[y][x]) {
				// 료이키텐카이 -> bfs 시작
				int cnt = 0;
				queue<pair<int, int>> q;
				q.push({ y,x });
				visited[y][x] = true;

				while (!q.empty()) {
					auto [cy, cx] = q.front();
					q.pop();
					cnt++;

					for (int dir = 0; dir < 4; dir++) {
						int ny = cy + dy[dir];
						int nx = cx + dx[dir];

						if (ny < 0 || ny >= M || nx < 0 || nx >= N) continue; // 범위 이상
						if (visited[ny][nx]) continue; // 방문 여부
						if (board[ny][nx] == 1) continue; // 직사각형 존재

						visited[ny][nx] = true;
						q.push({ ny, nx });
					}
				}

				areas.push_back(cnt);
			}
		}
	}

	sort(areas.begin(), areas.end());
	
	cout << areas.size() << endl;
	for (int i = 0; i < (int)areas.size(); i++) {
		cout << areas[i];
		if (i + 1 < (int)areas.size())
			cout << ' ';
	}
}