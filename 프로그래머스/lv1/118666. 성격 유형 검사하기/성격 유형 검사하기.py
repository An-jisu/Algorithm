def solution(survey, choices):
    answer = ''
    score = [3,2,1,0,1,2,3]
    #성격 유형에 따른 점수 매칭-딕셔너리
    dic = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M':0, 'A': 0, 'N':0}
    
    #survey 하나씩 돌면서(zip)/ 4보다 큰 경우 뒤에꺼에 더하고, 작거나 같은 경우 앞에꺼에 더함
    for i, j in zip(survey, choices):
        if j>4: #뒤에 꺼에 더함
            dic[i[1]]+=score[j-1]
        else:
            dic[i[0]]+=score[j-1]    
    #결과 출력(점수 큰 거, 같으면 알파벳 앞 순서)
    if dic['R']>=dic['T']:
        answer+='R'
    else:
        answer+='T'
    if dic['C']>=dic['F']:
        answer+='C'
    else:
        answer+='F'
    if dic['J']>=dic['M']:
        answer+='J'
    else:
        answer+='M'
    if dic['A']>=dic['N']:
        answer+='A'
    else:
        answer+='N'
    return answer