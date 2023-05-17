def solution(s):
    dic = {'p': 0, 'y': 0}
    for i in s:
        if i=='p' or i=='P':
            dic['p']+=1
        elif i=='y' or i=='Y':
            dic['y']+=1
    if dic['p']==dic['y']:
        return True
    else:
        return False