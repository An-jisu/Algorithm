def solution(id_list, report, k):
    answer = []
    #한 유저가 같은 유저 여러번 신고한 경우 신고 횟수 1회로 처리 (set으로 처리)
    report = list(set(report))
    #report 당한 수 딕셔너리로 (reported_dic)
    reported_dic = {}
    for i in report:
        a, b = i.split(' ')
        if b in reported_dic:
            reported_dic[b]+=1
        else:
            reported_dic[b]=1
    #k를 넘는 경우 새로운 리스트 배열에 넣음 (out)
    out = []
    for i,value in reported_dic.items():
        if value>=k:
            out.append(i)
    #report 다시 하나씩 접근하면서, 1번째 인덱스의 값이 위의 리스트에 존재하면 0번째 인덱스에 해당하는 딕셔너리 키값 증가시키기 (get_mail)
    get_mail = {}
    for i in id_list:
        get_mail[i]=0
    for i in report:
        a, b = i.split(' ')
        if b in out:
            get_mail[a]+=1
        else:
            continue
    #get_mail 딕셔너리의 value값 리스트로 반환
    return list(get_mail.values())