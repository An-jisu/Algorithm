def solution(N, stages):
    answer = []  #실패율 저장
    num = len(stages)  #각 스테이지에 남은 사람의 횟수 저장
    #N만큼 돌면서, stages에서 count해서 각 스테이지의 실패율 구하기
    for i in range(1,N+1):
        if num==0: 
            answer.append(0)
            continue
        cnt = stages.count(i) #각 스테이지의 실패한 사람의 횟수 구하기
        answer.append(stages.count(i)/num) #각 스테이지의 실패율 구해서 answer에 넣기
        num-=cnt #남은 사람의 횟수 조정
    #실패율 높은 것부터 스테이지 번호 내림차순 정렬하여 리스트 반환
    dic = {}
    for a , b in enumerate(answer):
        dic[a+1] = b
    return [i[0] for i in sorted(dic.items(), key = lambda x: x[1], reverse=True)]