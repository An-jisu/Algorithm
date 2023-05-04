def solution(cards1, cards2, goal):
    for i in goal:
        #cards1 리스트를 다 쓴 경우
        if (len(cards1)==0):
            #cards2 리스트에서 계속 비교해주면서, 다르면 return no
            if(i!=cards2[0]):
                return "No"
            else:
                del cards2[0]
            
        #cards2 리스트를 다 쓴 경우
        elif (len(cards2)==0):
            #cards1 리스트에서 계속 비교해주면서, 다르면 return no
            if(i!=cards1[0]):
                return "No"
            else:
                del cards1[0]
                
        #아직 둘 다 남아있는 경우 
        else:
            #cards1의 0번째나 cards2의 0번째에 없으면, return "No"/ 
            if (i!=cards1[0]) and (i!=cards2[0]):
                return "No"      
            else:
                #cards1에 있던 경우
                if (i==cards1[0]):
                    del cards1[0]
                #cards2에 있던 경우 
                if (i==cards2[0]):
                    del cards2[0]
        

        
    #반복문 끝까지 실행했으면, 모두 성공한 경우- return "Yes"
    return "Yes"