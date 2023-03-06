def solution(n):
    #n이 나누어떨어지는 소수들을 구하면 됨
    answer = []
    for i in range(2,n+1):
        count = 0
        for j in range(1,i+1):
            if i%j==0:
                count+=1
        if count==2 and n%i==0:
            answer.append(i)
    return sorted(answer)