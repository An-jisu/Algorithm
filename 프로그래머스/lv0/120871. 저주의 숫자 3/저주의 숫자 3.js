function solution(n) {
    var answer = 0;
    //n까지 반복하면서, 각 숫자에 해당하는 값이 3의 배수, 3이 들어가지 않는 수일 때까지 1더함
    for (var a = 1;a<=n;a++){
        answer+=1;
        while(answer%3===0 || (""+answer).includes('3')){
            answer+=1;
        }
    }
    return answer;
}