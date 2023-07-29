function solution(num, k) {
    let a = num.toString().split("").indexOf(k.toString());
    //문자열로 바꿔 배열의 각 요소로 분리하고,k의 인덱스에 1 더한 값을 반환
    return a===-1?a:a+1;
}