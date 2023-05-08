#기사 번호의 약수의 수에 해당하는 무기 구매하고자 -> 제한수치보다 큰 경우 거기서 정한 공격력의 무기 구매  : 무기를 구매하기 위한 철의 무개 return
#각 기사마다 구매할 무기의 무게 구해서(기사번호에 따른 약수의 갯수 기반) answer에 계속 더해줌
def solution(number, limit, power):
    answer = 0
    #기사들의 약수의 개수 구해서 리스트에 넣기-1부터 number까지)
    num = []
    for j in range(1, number+1):
        cnt = 0
        for i in range(1, int(j**0.5) +1 ):
            if j == i**2:
                cnt += 1
            elif j%i == 0:
                cnt += 2
        num.append(cnt)
                
    #리스트에 하나씩 접근하면서, 구매할 무기 무게 구해서 answer에 더함(limit 넘으면 power더함/아니면, 그냥 리스트의 값 더함)
    for i in range(number):
        if(num[i]>limit):
            answer+=power
            continue
        answer+=num[i]
    return answer