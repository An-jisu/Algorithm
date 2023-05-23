def solution(new_id):
    answer = ''
    #1단계
    new_id = new_id.lower()
    #2단계
    for i in new_id:
        if not(i=='-' or i=='_' or i=='.' or i.isalpha() or i.isdigit()):
            new_id=new_id.replace(i,'')

    #3단계
    for i in new_id:
        if answer[-1:]=='.' and i=='.':
            continue
        answer+=i
    #4단계
    if answer[:1]=='.':
        answer = answer[1:]
    if answer[-1:]=='.':
        answer = answer[:-1]
    #5단계
    if len(answer)==0:
        answer+='a'
    #6단계
    if len(answer)>=16:
        answer = answer[:15]
        if answer[-1:]=='.':
            answer = answer[:-1]
    #7단계
    if len(answer)<=2:
        while len(answer)<3:
            answer+=answer[-1]
    return answer