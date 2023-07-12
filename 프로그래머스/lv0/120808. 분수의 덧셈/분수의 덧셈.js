function solution(numer1, denom1, numer2, denom2) {
    //분모, 분자 각각 구하기
    let res_parent = denom1 * denom2;
    let res_son = (numer1*denom2) + (numer2*denom1);
    console.log(res_parent)
    console.log(res_son)
    
    //기약 분수로 나타내기 (최대 공약수로 나누기)
    const gcd = (a,b)=> (a%b === 0? b: gcd(b,a%b));
    console.log(gcd)
    
    //결과 반환
    return [res_son/gcd(res_son, res_parent), res_parent/gcd(res_son, res_parent)]
}