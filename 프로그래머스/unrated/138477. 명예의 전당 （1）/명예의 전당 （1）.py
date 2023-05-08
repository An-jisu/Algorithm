#명예의 전당에 k명의 사람을 올림(매일 그 날의 가수가 명예의 전당 k번째 사람보다 높으면 명예의전당으로-> k번째 명예의 전당 사람의 점수 배열 반환- 배열의 크기는 score의 수와 같을 것)
def solution(k, score):
    #가장 점수 적은 사람의 배열
    answer = []
    #명예의 전당 점수 들어갈 배열(k크기 만큼)
    top = []
    #score동안 반복문 돌면서, top의 마지막 인덱스의 값과 scroe의 값 비교하면서, 크면 2개 서로 바꾸고 오름차순 
    for i in range(len(score)):
        if len(top)<k:
            #top의 길이가 k보다 작으면 그냥 append
            top.append(score[i])
            #오름차순 정렬(sort)
            top.sort(reverse=True)
            #마지막 인덱스 사람 점수 answer에 append
            answer.append(top[-1])
            print(top)
        
        else:
            #top의 마지막 인덱스 값이 score의 i 인덱스 값보다 작으면 2개 바꿈
            if top[-1]<score[i]:
                top[-1]=score[i]
                top.sort(reverse=True)
            answer.append(top[-1])
            
    return answer