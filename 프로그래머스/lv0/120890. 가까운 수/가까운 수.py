def solution(array, n):
    answer = []
    array.sort()
    for i in array:
        answer.append(abs(n-i))
    box = [array[answer.index(min(answer))]]
    if len(box)>1:
        return min(box)
    else:
        return box[0]