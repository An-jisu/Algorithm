def solution(n, m, section):
    answer = 1
    paint = section[0]
    for i in section:
        if i -paint>=m:
            answer+=1
            paint = i
            
    return answer