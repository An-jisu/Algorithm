function solution(numlist, n) {
    var answer = [];
    var g = [];
    var gs = [];
    numlist.sort((a,b)=> b-a);
    // 절댓값 저장하기
    for (let b of numlist){
        g.push(b-n);
    }
    // 절댓값 배열 정렬
    gs = [...g].sort((a,b)=> Math.abs(a)-Math.abs(b));
    
    // 정렬 값에 따라 result에 값 넣기
    for (let v of gs){
        answer.push(numlist[g.indexOf(v)]);
    }
    return answer;
}