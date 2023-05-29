#최소 예산요구하는 사람들 먼저 지원해줌(총 예산 넘지 않을 때까지) 
def solution(d, budget):
    count = 0
    d.sort()
    i = 0
    while i<len(d) and budget>0 and budget>=d[i]:
        budget-=d[i]
        count+=1
        i+=1
        
    return count