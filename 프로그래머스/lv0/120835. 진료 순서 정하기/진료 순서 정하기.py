def solution(emergency):
    answer = list(0 for i in range(0,len(emergency)))
    for i in range(len(emergency)):
        maxNum = max(emergency)
        answer[emergency.index(maxNum)] = i+1
        emergency[emergency.index(maxNum)] = 0
    return answer