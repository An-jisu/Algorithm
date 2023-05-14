def solution(numbers):
    answer = 0
    #9까지 반복문 돌면서, numbers에 없으면 더해
    for i in range(1,10):
        if i not in numbers:
            answer+=i
    return answer