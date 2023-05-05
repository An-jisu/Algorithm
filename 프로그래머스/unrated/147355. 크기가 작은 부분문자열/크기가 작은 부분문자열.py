def solution(t, p):
    answer = 0
    #p의 자리수, p의 int값 저장하기
    p_len = len(p)
    p_int = int(p)
    #t에서 첫번째값부터 (len(t)-p의 자리수)만큼 접근하면서, 자리수만큼 씩 읽어들여서 p의 값보다 작거나 같은 경우에 answer에 +1
    for i in range(0, len(t)-p_len+1):
        if p_int>=int(t[i:i+p_len]): #리스트의 인덱싱으로 접근
            answer+=1
            
    return answer