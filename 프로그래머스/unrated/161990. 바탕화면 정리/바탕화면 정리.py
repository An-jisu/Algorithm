def solution(wallpaper):
    answer = []
    x = []
    y = []
    #x값, y값 각각 집합에 넣기(반복문 돌면서, #이면 i,j 값 넣기 )
    for i in range (len(wallpaper)):   
        for j in range (len(wallpaper[0])):  
            if(wallpaper[i][j]=="#"):
                x.append(i)
                y.append(j)

    #x의 최소, y의 최소/ x의 최대, y최소 구해서 넣기
    answer.append(min(x))
    answer.append(min(y))
    answer.append(max(x)+1)
    answer.append(max(y)+1)    
    
    return answer