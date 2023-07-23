function right(numbers){
    var answer = [];
    answer = numbers.slice(0,numbers.length-1);
    answer.unshift(numbers[numbers.length-1]);
    return answer;
}

function left(numbers){
    var answer = [];
    answer = numbers.slice(1,numbers.length);
    answer.push(numbers[0]);
    return answer;
}
function solution(numbers, direction) {
    var answer = [];
    answer = (direction==="right")? right(numbers): left(numbers);
    return answer;
}