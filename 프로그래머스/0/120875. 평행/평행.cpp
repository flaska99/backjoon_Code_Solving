#include <string>
#include <vector>

using namespace std;
// 두 선분의 차이가 같은 케이스가 있는지 탐색하는 문제
// 단, dots의 길이가 4로 고정 되어있어서 
// 조합의 개수도 케이스가 고정 
// 3개만 알아보면 됨 .

static inline bool cbn(
    const vector<vector<int>> & dot_vec, 
    int a, 
    int b, 
    int c, 
    int d
) {
  int x1 = dot_vec[a][0], y1=dot_vec[a][1];
  int x2 = dot_vec[b][0], y2=dot_vec[b][1];
  int x3 = dot_vec[c][0], y3=dot_vec[c][1];
  int x4 = dot_vec[d][0], y4=dot_vec[d][1];
  return (y2 - y1) * (x4 - x3) == (y4 - y3)*(x2 - x1);
}

int solution(vector<vector<int>> dots) {
    if (cbn(dots, 0,1,2,3)) return 1;
    if (cbn(dots, 0,2,1,3)) return 1;
    if (cbn(dots, 0,3,1,2)) return 1;
    return 0;
}