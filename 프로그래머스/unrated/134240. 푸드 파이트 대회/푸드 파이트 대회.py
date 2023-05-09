#음식의양 주어짐(칼로리 낮은 순서대로 길이가 음식의 양)-> 대회를 위한 배열로(양끝에서 칼로리작은값부터 똑같이 가운데쪽으로 증가하는 느낌-> 가운데는 물-0번 음식)
def solution(food):
    answer = ''
    #반복문 돌면서 음식의 양 조절/ food[i]의 절반값 만큼 answer에 더함
    for i in range(1, len(food)):
        #음식의 양 조절(홀수면 -1)- 1번 인덱스부터
        if not (food[i]%2==0):
            food[i] -=1
        for j in range (food[i]//2):
            answer+=str(i)

    return answer+'0'+answer[::-1]