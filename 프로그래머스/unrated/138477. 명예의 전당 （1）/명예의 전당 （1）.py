def solution(k, score):
    answer = []
    top = [] #명예의 전달 배열
    for i in score:
        top.append(i)
        
        if len(top)>k:
            top.remove(min(top))
        answer.append(min(top))
    return answer