#include <iostream>
#include <queue>
#include <vector>
#include <functional>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;

    cin >> n >> m;

    priority_queue<long long, vector<long long>, greater<long long>> pq;

    long long num;
    for(int i = 0; i < n; i++){
        cin >> num;
        pq.push(num);
    }

    while(m > 0) {
        long long a = pq.top(); pq.pop();
        long long b = pq.top(); pq.pop();
        long long s = a + b;
        pq.push(s);
        pq.push(s);

        m--;
    }

    long long sum = 0;
    while(!pq.empty()){
        sum += pq.top(); 
        pq.pop();
    }

    cout << sum;
    return 0;
}