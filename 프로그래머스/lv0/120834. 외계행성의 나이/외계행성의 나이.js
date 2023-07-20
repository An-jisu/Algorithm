function solution(age) {
    let a = ['a','b','c','d','e','f','g','h','i','j']
    let answer = []
    let b = age.toString().length
    for (let i = 0;i<b;i++){
        answer.push(a[age%10])
        age = parseInt(age/10)
    }

    return answer.reverse().join("")
}