def solution(A, B):
    count = 0
    C = A
    if A==B:
        return 0
    for i in range(len(A)):
        C = C[-1]+C[0:-1]
        if C==B:
            count+=1
            break
        count+=1
    if count==len(A):
        return -1
    else:
        return count