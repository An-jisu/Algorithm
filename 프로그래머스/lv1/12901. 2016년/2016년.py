def solution(a, b):
    date = [31,29,31,30,31,30,31,31,30,31,30,31]
    d = {0: 'THU', 1: 'FRI', 2: 'SAT',3: 'SUN',4: 'MON',5:'TUE',6:'WED'}
    
    return d[(sum(date[i] for i in range(a-1))+b)%7]