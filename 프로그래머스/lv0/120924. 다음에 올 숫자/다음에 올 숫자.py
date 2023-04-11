def solution(common):
    #등차수열인 경우 (0-1, 1-2 뺀 숫자가 같은 경우)
    if (common[1]-common[0]) == (common[2]-common[1]):
        return common[-1]+common[1]-common[0]
    
    #등비수열인 경우 (0-1, 1-2 나눈 숫자가 같은 경우)
    elif (common[1]//common[0]) == (common[2]//common[1]):
        return common[-1]*(common[1]//common[0])
