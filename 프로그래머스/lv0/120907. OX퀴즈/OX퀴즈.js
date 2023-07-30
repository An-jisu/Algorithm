function solution(quiz) {
    var answer = [];
    for (let a of quiz){
        //문자열을 분리
        let arr = a.split(" ");
        console.log(arr);
        //결괏값에 따라 answer에 넣기
        let u = arr[1]==='-'? Number(arr[0])-Number(arr[2]):Number(arr[0])+Number(arr[2]);
        u===Number(arr[4])? answer.push('O'):answer.push('X');
    }

    return answer;
}