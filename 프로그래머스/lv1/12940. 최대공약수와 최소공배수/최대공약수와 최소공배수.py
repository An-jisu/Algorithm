def solution(n, m):
    temp = []
    #최대 공약수
    for i in range(min(n,m),0,-1):
        if n%i==0 and m%i==0:
            temp.append(i)
            break
    #최소 공배수
    k = max(n,m)
    while(True):
        if k%n==0 and k%m==0:
            temp.append(k)
            break
        k+=max(n,m)
    return temp