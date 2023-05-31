def solution(babbling):
    answer = 0
    for i in babbling:
        #중복되는 경우있는 경우
        if 'aya'*2 in i or "ye"*2 in i or "woo"*2 in i or "ma"*2 in i:
            continue
        for j in ["aya", "ye", "woo", "ma"]:
            if j in i:
                i = i.replace(j, ' ')
        i = i.replace(' ', '')
        if len(i)==0:
            answer+=1
    return answer