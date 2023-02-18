def solution(numer1, denom1, numer2, denom2):
    numer1 = numer1*denom2 
    numer2 = numer2*denom1   
    res_son = numer1 + numer2
    res_parent = denom1*denom2

    res = min(res_son, res_parent)
    
    for i in range(res+1,1,-1):
        if((res_son)%i ==0) and (res_parent%i==0):
            res_son = res_son/i
            res_parent = res_parent/i

    answer = [res_son, res_parent]
    return answer