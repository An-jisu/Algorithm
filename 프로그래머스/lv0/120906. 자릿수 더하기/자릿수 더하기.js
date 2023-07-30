function solution(n) {
    let sum = 0;
    return (''+n).split("").reduce((acc, cur) => acc+Number(cur),0);
}