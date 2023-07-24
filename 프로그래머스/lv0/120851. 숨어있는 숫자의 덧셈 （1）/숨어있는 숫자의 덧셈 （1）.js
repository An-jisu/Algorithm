function solution(my_string) {
    //split하고, 자연수 인경우 계속 누적해서 더해준다. 
    return my_string.split("").filter(a=>Number.isInteger(Number(a))).map(a=> Number(a)).reduce((acc, cur)=> acc+cur);
}