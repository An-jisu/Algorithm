t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for i in range(n)]
    red = []
    result = 0
    # 빨간 영역을 배열에 넣어놓기
    for i in arr:
        if i[-1] == 1:
            for row in range(i[0], i[2]+1):
                for col in range(i[1], i[3]+1):
                    red.append((row, col))
    # 파란색의 좌표들 하나씩 따라가면서 빨간 영역에 속하면 +1
    for i in arr:
        if i[-1] == 2:
            for row in range(i[0], i[2]+1):
                for col in range(i[1], i[3]+1):
                    if (row, col) in red:
                        result+=1

    print(f"#{test_case} {result}")