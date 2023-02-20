import math
def solution(money):
    rem = money
    count = 0
    while(rem>=0):
        rem = rem-5500
        count+=1
    rem+=5500
    count-=1
    return [count, money-(5500*count)]