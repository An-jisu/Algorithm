from itertools import combinations
def solution(nums):
    answer = 0
    for i in list(set(combinations(nums, 3))):
        count = 0
        for j in range(1, sum(i)):
            if sum(i)%j==0:
                count+=1
        if count==1:
            print(i)
            answer+=1

    return answer