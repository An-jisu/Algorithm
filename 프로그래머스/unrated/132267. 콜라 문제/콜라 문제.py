#a개의 빈병을 마트에 주면, b개의 병을 줌/ 현재n개 가지고 있을 때 받을 수 있는 콜라 수 반환
def solution(a, b, n):
    answer = 0
    while n>=a: #n이 a보다 크거나 같은 동안 반복 (m: 몫, r: 나머지)
        m = n//a  
        r = n%a    
        #n을 a로 나눈 것의 몫을 계속 더해줌
        answer+=(m*b)   
        #n을 업데이트 (몫+나머지)
        n = r+(m*b)   
    return answer