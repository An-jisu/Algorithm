def solution(n):
    answer = 0
    return (n**0.5+1)**2 if n**0.5/int(n**0.5)==1 else -1