def solution(babbling):
    answer = 0
    w = ["aya","ye","woo","ma"]
    #요소 하나씩 접근하면서 존재하면 count 하고 그 문자열 삭제
    for i in babbling:
        print(i)
        for j in w:
            if i=='':
                break
            elif j in i:
                #삭제
                i = i.replace(j, ' ')
                print(i)
        #공백이면 count
        i = i.replace(' ','')
        if i=='':
            answer+=1
    return answer