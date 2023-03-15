def solution(numbers):
    max_m, max_p = 0, 0
    numbers.sort()
    max_m = numbers[0]*numbers[1]
    max_p = numbers[len(numbers)-1]*numbers[len(numbers)-2]
    
    return max(max_m, max_p)