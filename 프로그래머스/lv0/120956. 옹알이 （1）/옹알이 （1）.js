function solution(babbling) {
    var answer = 0;
    for (var a of babbling){
        var arr = []
        var count = 0;
        arr = a.split(/aya|ye|ma|woo/)
        for (var b of arr){
            if (b!==''){
                count+=1
            }
        }
        if (count===0){
            answer+=1;
        }
    }
    return answer;
}