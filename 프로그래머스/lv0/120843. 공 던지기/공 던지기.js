function solution(numbers, k) {
    let idx = 0;
    for(let i = 0;i<k-1;i++){
        if ((idx+2)===numbers.length){
            idx = 0;
        }
        else if((idx+2)===numbers.length+1){
            idx = 1;
        }
        else{
            idx+=2;
        }
    }
    return numbers[idx];
}