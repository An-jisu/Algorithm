def solution(park, routes):
    #현재 위치(now), park 가로 세로 길이 저장
    x = y =0 #변화되는 x,y값 
    now = []
    row = len(park)
    col = len(park[0])

    for i in range(row):
        for j in range(col):
            if(park[i][j]=='S'):
                now.append(i)
                x = i
                now.append(j)
                y = j
                break
    
    #routes의 수만큼 반복문 돌면서 park 크기보다 크거나 장애물 만나면 현재위치 저장하지 않음
    for i in routes:
        dir, num = i.split(" ")
        num = int(num)
        mons = []
        if (dir=='S'):
            if(x+num>row-1):
                continue
            else:  
                for j in range(x+1, x+num+1):
                    mons.append(park[j][y])
                if 'X' in mons:
                    continue
                else:
                    x+=num
                    
        elif (dir=='E'):
            if(y+num>col-1):
                continue
            else:
                for j in range(y+1, y+num+1):
                    mons.append(park[x][j])
                if 'X' in mons:
                    continue
                else:
                    y+=num
                
        elif (dir=='W'):
            if(y-num<0):
                continue
            else:
                for j in range(y-num, y):
                    mons.append(park[x][j])
                if 'X' in mons:
                    continue
                else:
                    y-=num

        elif (dir=='N'):
            if(x-num<0):
                continue
            else:
                for j in range(x-num, x):
                    mons.append(park[j][y])
                if 'X' in mons:
                    continue
                else:
                    x-=num

        now[0] = x
        now[1] = y

    return now