#잃어버린 학생 중, 체육복을 빌릴 수 있는 학생 수 구하는 게 관건
def solution(n, lost, reserve):
    #여벌 옷 가져온 학생이 도난 당함(빌릴 필요도, 빌려줄 수도 없으므로 제거)
    a = (set(lost) & set(reserve))
    answer = n-len(lost)+len(a)
    reserve = list(set(reserve)-a) 
    lost = list(set(lost)-a)
    #lost돌면서, reserve에 1개 더 작거나 큰 값 존재하면, 갯수 증가
    for i in lost:
        if i-1 in reserve:
            answer+=1
            reserve.remove(i-1)
        elif i+1 in reserve:
            answer+=1
            reserve.remove(i+1)
            
    return answer