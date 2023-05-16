def solution(lottos, win_nums):
    answer = []
    count = 0
    #일치하는 것의 개수 세기
    for i in lottos:
        if i in win_nums:
            count+=1
    #0의 수 세기
    num_zero = lottos.count(0)
    
    #일치하는 것의 수, 0의 수에 따라 결과 반환(최고순위: 합, 최저순위: 일치하는 것의 수)
    if num_zero==0:
        if count==0:
            return [6,6]
        else:
            return [7-count,7-count]
    elif num_zero==6:
        return [1,6]
    else:
        return [7-(count+num_zero), 7-count]