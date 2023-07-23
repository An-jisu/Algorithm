function solution(numbers) {
    //오름차순 정렬
    numbers.sort((a,b)=>a-b);
    console.log(numbers);
    //끝의 두 값 곱해서 반환
    return numbers[numbers.length-1]*numbers[numbers.length-2];
}