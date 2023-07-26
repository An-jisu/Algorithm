function solution(order) {
    var answer = 0;
    //문자열로 바꾸고, 하나씩 검사하면서 3,6,9이면 answer값 증가
    let s = String(order);
    return s.split("").filter((a)=> Number(a)%3===0&&a!=='0').length;
}