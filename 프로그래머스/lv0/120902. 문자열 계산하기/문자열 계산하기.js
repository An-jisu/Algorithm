function solution(my_string) {
    let arr = my_string.split(" ");
    let result = Number(arr[0]);
    for(let i = 1;i<arr.length;i+=2){
        result = (arr[i]==='+')? result+Number(arr[i+1]): result-Number(arr[i+1]);
    }
    return result;
}