def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        numbers[i] *=2
        answer.append(numbers[i])
    return answer