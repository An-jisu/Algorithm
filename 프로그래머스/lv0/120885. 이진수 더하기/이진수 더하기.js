function solution(bin1, bin2) {
    var answer = '';
    if (bin1=="0"&&bin2=="0"){
        return "0"
    } 
    //bin1 10진수로 바꾸기
    var a1 = 0;
    for (var k = bin1.length-1;k>=0;k--){ 
        a1+=Number(bin1[bin1.length-1-k])*(2**k); 
    }
    console.log(a1)
    //bin2 10진수로 바꾸기
    var a2 = 0;
    for (var k = bin2.length-1;k>=0;k--){ 
        a2+=Number(bin2[bin2.length-1-k])*(2**k); 
    }
    console.log(a2)
    //2개의 합 다시 구해서 2진수로 
    var result = a1+a2;
    var arr = []
    while (result>0){
        arr.push(result%2)
        result = Math.floor(result/2)
    }
    return arr.reverse().join('');
}