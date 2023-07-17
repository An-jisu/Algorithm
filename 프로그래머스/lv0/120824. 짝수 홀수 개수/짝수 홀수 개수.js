function solution(num_list) {
    let result = new Array(2).fill(0)
    for (let a of num_list){
        if (a%2===0){
            result[0]+=1
        }
        else{
            result[1]+=1
        }
    }
    return result
}