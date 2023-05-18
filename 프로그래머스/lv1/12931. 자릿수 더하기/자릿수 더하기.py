def solution(n):
    answer = 0
    a = n
    while a>0:
        a, b = divmod(a,10)
        answer+=b
    return answer