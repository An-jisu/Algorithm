function factorial(n){
    let sum = 1;
    for (let i =1;i<=n;i++){
        sum*=i;
    }
    return sum;
}

function solution(n) {
    let s = 1;
    while (factorial(s)<=n){
        s+=1
    }
    return s-1;
}