def solution(array):
    count_num=[0] * (max(array)+1)
    #배열의 모든 요소 검사하면서, 그 요소에 해당하는 인덱스값 증가
    for i in array:
        count_num[i] +=1
        
    #가장 최댓값 저장
    max_num = max(count_num)
    
    #최댓값에 해당하는 값이 2개 이상이면 return -1
    if(count_num.count(max_num)>1):
        return -1
    #그렇지 않으면, 그것의 인덱스 반환
    else:
        return count_num.index(max_num)