def solution(polynomial):
    x, con = 0, 0
    
    # 공백을 기준으로 분리
    polynomial = polynomial.replace(' ', '').split('+')
    for i in polynomial:
        if 'x' in i:
            if len(i)>1:
                x+=int(i[:-1])
            else:
                x+=1
        else:
            con+=int(i)
    
    if x==0:
        if con==0:
            return '0'
        else:
            return str(con)
    elif x==1:
        if con==0:
            return 'x'
        else:
            return 'x + ' + str(con)
    else:
        if con==0:
            return str(x)+'x'
        else:
            return str(x)+'x + ' +str(con)