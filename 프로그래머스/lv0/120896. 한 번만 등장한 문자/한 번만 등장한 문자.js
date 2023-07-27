function count(s, c){
    let count = 0;
    //s의 문자 하나씩 접근하면서, c와 같으면 count
    for (let a of s){
        if(a===c){
            count++;
        }
    }
    return count;
}

function solution(s) {
    //중복 제거 후, 오름차순 정렬한다.
    return s.split("").filter((a)=> (count(s,a)===1)).sort().join("");
}