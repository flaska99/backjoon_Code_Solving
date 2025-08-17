#include <string>
#include <vector>

using namespace std;

string solution(string X, string Y) {
    int cx[10] = {0}, cy[10] = {0};
    for (char ch : X) cx[ch - '0']++;
    for (char ch : Y) cy[ch - '0']++;
    
    string answer;
    
    for (int d = 9; d >= 0; --d){
        int k = min(cx[d], cy[d]);
        if (k > 0) answer.append(k, char('0' + d));
    }
    
    if (answer.empty()) return "-1";
    if (answer[0] == '0') return "0";
    
    return answer;
}