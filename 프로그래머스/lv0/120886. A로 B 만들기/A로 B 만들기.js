function solution(before, after) {
    //before 정렬한 것, after 정렬한 것 같으면 1 아니면 0 반환
    return [...before].sort().join("")===[...after].sort().join("")? 1:0;
}