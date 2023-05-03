def solution(name, yearning, photo):
    answer = []
    #그리움 점수를 딕셔너리로 
    miss = {name:i for name, i in zip(name, yearning)}
    #사진의 수만큼(photo의 길이) 반복문 돌면서, 각 사진의 추억 점수 계산해서 answer에 append
    for i in photo:
        sum = 0
        for j in i:
            if(j in miss):
                sum+=miss[j]
        answer.append(sum)
    
    
    return answer