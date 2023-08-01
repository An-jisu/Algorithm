function solution(array) {
    let sum = 0;
    for (let a of array){
        sum+=(''+a).split("").filter((b)=> b==='7').length;
    }
    return sum;
}