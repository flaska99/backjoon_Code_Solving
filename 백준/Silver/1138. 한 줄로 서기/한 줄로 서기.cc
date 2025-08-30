#include <iostream>
#include <vector>

using namespace std;

int main(){
    int N;
    if(!(cin >> N)) return 0;

    vector<int> arr(N); 
    for(int i = 0; i < N; ++i) cin >> arr[i];

    vector<int> answer;
    for(int i = N; i >= 1; i--) {
        int a = arr[i-1];
        answer.insert(answer.begin() + a, i);
    }

    for (int x : answer) cout << x << " ";
}
