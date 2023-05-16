def solution(lottos, win_nums):
    rank = [6,6,5,4,3,2,1]
    count = 0
    #일치하는 것의 개수 세기
    for i in lottos:
        if i in win_nums:
            count+=1
    #0의 수 세기
    num_zero = lottos.count(0)
    
    #일치하는 것의 수, 0의 수에 따라 결과 반환(최고순위: 합, 최저순위: 일치하는 것의 수)
    return rank[count + num_zero],rank[count]