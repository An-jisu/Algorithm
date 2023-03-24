def solution(sides):
    answer = 0
    #나머지 한 변이 가장 긴 변인 경우- (while-max+1부터 시작해서, 나머지 2개의 합보다 크거나 같아지면 break, 아니면 count)
    i = max(sides)+1
    while(1):
        if(i>=sum(sides)):
            break
        answer+=1
        i+=1
    print(answer)
    #나머지 한 변이 가장 긴 변이 아닌 경우- max-1부터 시작하면서, m이 더 커지면 반복 끝
    j = max(sides)
    while(1):
        if(max(sides)>=j+sum(sides)-max(sides)):
            break
        answer+=1
        j-=1
    print(answer)
    return answer       