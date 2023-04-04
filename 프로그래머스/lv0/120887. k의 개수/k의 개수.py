def solution(i, j, k):
    answer = 0
    for u in range(i, j+1):
        if str(k) in str(u):
            for h in str(u):
                if h == str(k):
                    answer+=1
        else:
            continue
    return answer