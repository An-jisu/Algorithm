def solution(chicken):
    #총 쿠폰 수 계산(chicken: 서비스로 받게되는 쿠폰 수, rem: 남는 쿠폰, answer: 총 서비스 수)
    answer = 0
    div = 0
    rem = 0
    while chicken//10!=0:
        div = chicken//10
        rem = chicken%10
        answer+=div
        chicken = div+rem

    #최대 서비스 개수 반환 
    return answer