function solution(my_string) {
    //문자열에서 숫자만 filter하고(int인 것만 남기기), sort하기
    return my_string.split("").filter(a=> Number.isInteger(Number(a))).map(b => Number(b)).sort((a,b)=> a-b);
}