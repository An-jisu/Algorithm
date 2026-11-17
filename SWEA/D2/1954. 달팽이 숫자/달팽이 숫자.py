t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    arr = [[0]*n for _ in range(n)]
    # print(f"#{test_case} {n} {arr}")
    r1, c1 = 0, 0
    direc = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    curDir = 0
    #값 넣고, 다음 위치가 끝을 벗어나거나 값이 있으면 방향전환 / else: 현재 방향으로 위치 이동
    for i in range(n*n):
        arr[r1][c1] = i+1
        # print(r1, c1, arr)
        next_r = r1+direc[curDir][0]
        next_c = c1+direc[curDir][1]
        # print(next_r, next_c)
        if next_r >= n or next_c>= n or arr[next_r][next_c] !=0: # 값이 있으면도 추가
            curDir = (curDir+1)%4
            # print(f"change!! {curDir}")
        r1 +=direc[curDir][0]
        c1+=direc[curDir][1]
    print(f"#{test_case}")
    for i in arr:
        print(*i)