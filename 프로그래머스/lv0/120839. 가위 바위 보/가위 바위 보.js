function solution(rsp) {
    var answer = '';
    let a = Array.from(rsp.split(""));
    for (b of a){
        if (Number(b)===2){
            answer+='0';
        }
        else if(Number(b)===0){
            answer+='5';
        }
        else{
            answer+='2';
        }
    }
    return answer;
}