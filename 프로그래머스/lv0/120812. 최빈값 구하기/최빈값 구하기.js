function solution(array) {
    //1000개짜리 배열 선언
    var a = new Array(1000).fill(0);    
    //for문 돌면서 그 배열에 해당하는 배열 값 증가시켜
    for(let i = 0;i<array.length;i++){
        a[array[i]]++;
    }
    //그 배열의 최댓값 구하기
    const maxValue = Math.max.apply(null,a);
    console.log(maxValue)
    //최댓값이 2개이상이면 -1 return
    var count = 0;
    a.map(item => {
        if (item===maxValue){
            count++;
        }
    })
    if (count>1){
        return -1
    }
    //그렇지 않으면 그 최댓값의 인덱스 값 return
    else {
        return a.indexOf(maxValue)
    }
}