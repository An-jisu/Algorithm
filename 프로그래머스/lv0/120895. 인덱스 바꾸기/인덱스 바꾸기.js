function solution(my_string, num1, num2) {
    var answer = my_string.split("");
    let temp = answer[num1];
    answer[num1] = answer[num2];
    answer[num2] = temp;
    return answer.join('');
}