def solution(players, callings):
    #딕셔너리 사용
    idx = {i:player for i, player in enumerate(players)} # 등수: 선수 
    p = {player:i for i, player in enumerate(players)} # 선수: 등수
    for i in callings: 
        #선수의 등수 (현재 선수, 앞 선수)
        num1 = p[i]  #현재 선수의 등수
        num2 = p[i]-1 #앞 선수의 등수 
        i2 = idx[num2] # 앞 선수
        
        #등수에 따른 선수 교체
        idx[num1] = i2 #앞 선수의 등수 하나 뒤로 밀려남
        idx[num2] = i
        
        #등수도 교체
        p[i] = num2
        p[i2] = num1
        
    #등수에 따른 선수 이름 값 list로 반환
    return list(idx.values())