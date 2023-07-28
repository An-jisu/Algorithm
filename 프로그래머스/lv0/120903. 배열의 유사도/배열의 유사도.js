function solution(s1, s2) {
    let set = new Set((s1+','+s2).split(","));
    return ((s1+','+s2).split(",").length)-(set.size);
}