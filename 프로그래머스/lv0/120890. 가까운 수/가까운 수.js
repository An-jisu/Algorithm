function solution(array, n) {
    var arr = [];
    array.sort((a,b)=>a-b);
    //차잇값을 배열에 넣기
    for (let a of array){
        arr.push(Math.abs(a-n));
    }
    //차잇값 가장 적은 첫번째 값 return 
    return array[arr.indexOf(Math.min(...arr))];
}