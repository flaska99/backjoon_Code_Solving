#include <iostream>
#include <queue>
using namespace std;

int main() 
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int n, h, t;// 거인의 나라 인구수 / 센티의 키 / 뿅망치 횟수 제한
	// 뿅망치를 맞게 된다면 (키 / 2) 로 키가 줄음


	cin >> n >> h >> t;

	priority_queue<long long> pq;

	// 각 거인의 키는 n만큼 한 줄로 입력됨.

	for (int i = 0; i < n; i++) {
		long long x; cin >> x;
		pq.push(x);
	}
	
	int cnt = 0;

	while ((t--) && (pq.top() >= h) && (pq.top() > 1)) {
		long long top = pq.top(); pq.pop();
		pq.push(top / 2); // 뿅망치 사용
		cnt++;			  // 횟수 증가
	}

	if (pq.top() < h)
		cout << "YES\n" << cnt << endl;
	else
		cout << "NO\n" << pq.top() << endl;

}