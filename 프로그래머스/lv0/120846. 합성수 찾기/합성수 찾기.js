function solution(n) {
    var answer = 0;
    for (let i = 2;i<=n;i++){ //n까지 하나씩 접근
        let c = 0;
        //합성수 구하기(2부터 제곱근 값 사이의 값 중 i로 나누어떨어지는 수 있으면 합성수)
        for(let j=2;j<=i**0.5;j++){
            if(i%j===0){
                c+=1;
            }
        }
        if (c>=1){ 
            answer+=1;
        }
    }
    
    return answer;
}