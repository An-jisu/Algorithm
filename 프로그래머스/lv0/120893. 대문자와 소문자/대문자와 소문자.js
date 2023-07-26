function solution(my_string) {
    var answer = '';
    my_string.split("").map((a)=> a===a.toUpperCase()? answer+=a.toLowerCase():answer+=a.toUpperCase());
    return answer;
}