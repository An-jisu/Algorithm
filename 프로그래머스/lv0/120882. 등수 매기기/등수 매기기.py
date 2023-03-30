def solution(score):
    answer = []
    result = []
    #평균내서 배열에 담기
    for i in score:
        answer.append((i[0]+i[1])/2)
    #등수 매기기
    s = sorted(answer, reverse=True)
    for i in answer:
        result.append(s.index(i)+1)
    return result