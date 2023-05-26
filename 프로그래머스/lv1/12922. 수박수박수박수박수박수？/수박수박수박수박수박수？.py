def solution(n):
    a = "수박"
    answer =''
    for i in range(n):
        if i%2==0:
            answer+=a[0]
        else:
            answer+=a[1]
    return answer