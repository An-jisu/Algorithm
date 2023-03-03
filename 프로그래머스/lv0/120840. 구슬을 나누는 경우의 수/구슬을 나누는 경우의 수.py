def fac(a):
    mul = 1
    for i in range(1,a+1):
        mul*=i
    return mul
    
def solution(balls, share):
    return fac(balls)/(fac(balls-share)*fac(share))   