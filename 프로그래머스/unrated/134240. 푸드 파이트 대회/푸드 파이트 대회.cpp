#include <string>
#include <vector>

using namespace std;

string solution(vector<int> food) {
    string answer = "0";
    int a;
    for(int i = food.size()-1;i>0;i--){
        a = food[i]/2;
        while (a>0){
            answer = to_string(i) + answer + to_string(i);
            a-=1;
        }
    }
    return answer;
}
