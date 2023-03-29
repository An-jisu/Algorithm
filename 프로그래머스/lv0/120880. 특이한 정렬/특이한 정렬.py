import math
def solution(numlist, n):
    #차이가 같은 경우 큰 수를 먼저 저장해준다는 조건을 만족시키기 위해
    numlist.sort(reverse=True)

    #차이의 절댓값을 리스트에 저장
    diff = []
    for i in range(0,len(numlist)):
        diff.append(abs(n-numlist[i]))

    #작은 것의 인덱스에 해당하는 값을 새로 배열에 다시 추가
    answer = []
    while len(diff)!=0:
        a = diff.index(min(diff))
        answer.append(numlist[a])
        del diff[diff.index(min(diff))]
        del numlist[a]

    return answer
    