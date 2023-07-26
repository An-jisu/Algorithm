function solution(cipher, code) {
    var answer = '';
    cipher.split("").map((a,b)=> (b+1)%code===0? answer+=a:answer+='');
    return answer;
}