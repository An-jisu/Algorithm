def solution(dots):
    g,s = 0, 0
    # 첫번째 좌표와, 그것과 x좌표가 같은 좌표를 찾아 세로 길이 구하기
    # 첫번째 좌표와 그것과 y좌표가 같은 좌표를 찾아 가로 길이 구하기
    for i in dots:
        if dots[0][0]==i[0]:
            s = abs(dots[0][1]-i[1])
        if dots[0][1] ==i[1]:
            g = abs(dots[0][0]-i[0])
    return s*g