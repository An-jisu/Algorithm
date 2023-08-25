function solution(chicken) {
    var answer = 0, cou = chicken;
    //쿠폰 수가 10개 이하가 될 때까지 계속 10을 빼주고, answer 1 더하고, 쿠폰 수 1더해
    while (cou>=10){
        cou-=10;
        answer+=1;
        cou+=1
    }
    return answer;
}