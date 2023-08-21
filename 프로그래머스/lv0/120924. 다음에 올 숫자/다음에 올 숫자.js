function solution(common) {
    return (common[1]-common[0]===common[2]-common[1])?common[common.length-1]+common[1]-common[0]:common.slice(-1)*Math.floor(common[1]/common[0]);
}