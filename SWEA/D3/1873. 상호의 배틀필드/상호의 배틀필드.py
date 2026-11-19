t = int(input())
for test_case in range(1, t+1):
    h, w = map(int, input().split())
    gameMap = [list(map(str, input())) for _ in range(h)]
    n = int(input())
    inputs = input()
    # print(h, w, gameMap, n, inputs)
    dir = ['^', 'v', '<', '>']

    # 현재 전자의 위치 구하기
    for i in range(h):
        for j in range(w):
            if gameMap[i][j] in dir:
                row = i
                col = j
                currentDir = gameMap[i][j]
    # print(row, col)

    # 명령어들 처리하기
    for user in inputs:
        # print(row, col)
        # print(user)
        if user == 'U':
            currentDir = '^'
            gameMap[row][col] = currentDir
            # 현재 위의 값이 바깥으로 벗어나지 않으면서, 평지인 경우 이동 (위의 값 바꾸고, 현재값 평지값으로)
            if row-1 >= 0:
                if gameMap[row-1][col] =='.':
                    gameMap[row][col] = '.'
                    gameMap[row - 1][col] = currentDir
                    row-=1

        elif user == 'D':
            currentDir = 'v'
            gameMap[row][col] = currentDir
            # 현재 아래의 값이 바깥으로 벗어나지 않으면서, 평지인 경우 이동 (아래의 값 바꾸고, 현재값 평지값으로)
            if row+1 <= h-1:
                if gameMap[row+1][col] =='.':
                    gameMap[row][col] = '.'
                    gameMap[row + 1][col] = currentDir
                    row+=1

        elif user == 'L':
            currentDir = '<'
            gameMap[row][col] = currentDir
            # 현재 왼쪽의 값이 바깥으로 벗어나지 않으면서, 평지인 경우 이동 (왼쪽의 값 바꾸고, 현재값 평지값으로)
            if col-1 >= 0:
                if gameMap[row][col-1] =='.':
                    gameMap[row][col] = '.'
                    gameMap[row][col-1] = currentDir
                    col-=1

        elif user == 'R':
            currentDir = '>'
            gameMap[row][col] = currentDir
            # 현재 아래의 값이 바깥으로 벗어나지 않으면서, 평지인 경우 이동 (아래의 값 바꾸고, 현재값 평지값으로)
            if col+1 <= w-1:
                if gameMap[row][col+1] =='.':
                    gameMap[row][col] = '.'
                    gameMap[row][col+1] = currentDir

                    col+=1

        elif user == 'S':
            prow, pcol = row, col
            if currentDir == '^':
                while prow > 0:
                    prow -=1
                    if gameMap[prow][pcol] == '*':
                        gameMap[prow][pcol] = '.'
                        break
                    elif gameMap[prow][pcol] == '#':
                        break

            elif currentDir == 'v':
                while prow < h-1:
                    prow +=1
                    if gameMap[prow][pcol] == '*':
                        gameMap[prow][pcol] = '.'
                        break
                    elif gameMap[prow][pcol] == '#':
                        break
            elif currentDir == '<':
                while pcol > 0:
                    pcol -=1
                    if gameMap[prow][pcol] == '*':
                        gameMap[prow][pcol] = '.'
                        break
                    elif gameMap[prow][pcol] == '#':
                        break
            elif currentDir == '>':
                while pcol < w-1:
                    pcol +=1
                    if gameMap[prow][pcol] == '*':
                        gameMap[prow][pcol] = '.'
                        break
                    elif gameMap[prow][pcol] == '#':
                        break
        # for i in gameMap:
        #     print(*i)
        # print()

    print(f"#{test_case}", end=" ")
    for i in gameMap:
        print(''.join(i))