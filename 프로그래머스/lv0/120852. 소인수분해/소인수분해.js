function solution(n) {
    var answer = [];
    let a = 2;
    while (n>1){
        while (n%a===0){
            if (!answer.includes(a)){
                answer.push(a);
            }
            n=n/a;
        }
        a++;
    }
    return answer;
}