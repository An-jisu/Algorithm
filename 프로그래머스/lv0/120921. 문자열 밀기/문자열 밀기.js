function solution(A, B) {
    var count = 0;
    // 문자열의 길이만큼 반복하면서, 오른쪽으로 밀면서 count하기. 같아지면 반복 종료.
    for (var a = 0;a<A.length;a++){
        if(A===B){
            return count
        }
        A = A[A.length-1]+A.slice(0,A.length-1)
        count+=1
    }
    return -1;
}