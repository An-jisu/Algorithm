function solution(i, j, k) {
    return ([...Array(j)].map((_,i)=> i+1).filter((a)=> a>=i).join("").toString().split("").filter((b)=>b===(k+"")).length);
}