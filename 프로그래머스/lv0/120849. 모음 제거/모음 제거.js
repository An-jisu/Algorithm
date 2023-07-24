function solution(my_string) {
    var answer = ['a','e','i','o','u'];
    answer = my_string.split("").filter(a => !answer.includes(a)).join("");
    return answer;
}