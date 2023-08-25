function solution(score) {
    var answer = [];
    var s = [];
    //평균값으로 배열에 넣기
    for(var i =0;i<score.length;i++){
        score[i] = (score[i][0]+score[i][1])/2;
    }
    s = [...score].sort((a,b)=>b-a);
    for (let a of score){
        answer.push(s.indexOf(a)+1)
    }
    return answer;
}