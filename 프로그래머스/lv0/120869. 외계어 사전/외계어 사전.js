function solution(spell, dic) {
    for (var a of (dic.filter((k)=> k.length===spell.length))){
        //dic요소 정렬한 것과 spell정렬해서 join한 것 같으면 1 return 아니면 2
        if (a.split("").sort().join("")===spell.sort().join("")){
            return 1;
        }
        else {
            continue;
        }
    }
    return 2;
}