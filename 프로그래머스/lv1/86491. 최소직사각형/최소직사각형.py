def solution(sizes):
    g = []
    s = []
    #각각의 명함을 내림차순으로 정렬하여 각 가로, 세로의 최댓값의 곱 return
    for i in sizes:
        i.sort(reverse=True)
        g.append(i[0])
        s.append(i[1])
    #가로, 세로를 각각의 배열에 넣기 -> 최댓값 구해서 곱 반환
    return max(g)*max(s)