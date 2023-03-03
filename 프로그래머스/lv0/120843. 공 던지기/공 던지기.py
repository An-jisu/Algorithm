def solution(numbers, k):
    answer = 1
    for i in range(k-1):
        if(answer==len(numbers)-1):
            answer = 1
            continue
        elif(answer==len(numbers)):
            answer = 2
            continue
        else:
            answer +=2
    return answer