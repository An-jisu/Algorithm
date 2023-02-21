def solution(num_list):
    count_even = 0
    count_odd = 0
    for i in num_list:
        if(i%2==0):
            count_even+=1
        else:
            count_odd+=1
    return [count_even, count_odd]