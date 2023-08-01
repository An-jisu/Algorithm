function solution(my_str, n) {
    var answer = [];
    for(let a = 0;a<my_str.length;a=a+n){
        console.log();
        answer.push(my_str.slice(a,a+n));
    }
    return answer;
}