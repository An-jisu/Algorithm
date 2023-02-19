def solution(n):
    x = 1
    while((n*x)%6!=0):
        x+=1
    return (n*x)//6