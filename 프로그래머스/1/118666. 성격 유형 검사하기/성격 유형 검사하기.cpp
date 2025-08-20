#include <string>
#include <vector>
#include <map>

using namespace std;

string solution(vector<string> survey, vector<int> choices) {
    map<char, int> score;
    score['R'] = score['T'] = 0;
    score['C'] = score['F'] = 0;
    score['J'] = score['M'] = 0;
    score['A'] = score['N'] = 0;
    
    for (int i = 0; i < survey.size(); i++) {
        char left = survey[i][0];
        char right = survey[i][1];
        int choice = choices[i];
        
        choice < 4 ? score[left] += 4 - choice : score[right] += choice - 4;
    }
    
    string res = "";
    
    res += (score['R'] >= score['T'] ? 'R' : 'T');
    res += (score['C'] >= score['F'] ? 'C' : 'F');
    res += (score['J'] >= score['M'] ? 'J' : 'M');
    res += (score['A'] >= score['N'] ? 'A' : 'N');
    
    return res;
}
