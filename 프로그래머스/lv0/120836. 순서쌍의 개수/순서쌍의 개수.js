function solution(n) {
    var answer = 0;
    for (let i = 0;i<=n**0.5;i++){
        if (n%i===0){
            answer+=1
        }
    }
    if (parseInt(n**0.5)**2===n){
        return answer*2-1
    }
    else{
        return answer*2
    }
    return answer*2
}