function solution(numbers) {
    var arr = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'];
    for (let a = 0;a<10;a++){
        if (numbers.includes(arr[a])){
            numbers = numbers.replaceAll(arr[a], a)
        }
    }
    return Number(numbers);
}