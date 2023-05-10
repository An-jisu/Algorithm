def solution(price, money, count):
    a = sum([price*i for i in range(1, count+1)])-money
    if a<=0:
        return 0
    else:
        return a