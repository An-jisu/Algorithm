dr = [-1, 1, 0, 0, -1, -1, 1, 1]
dc = [0, 0, -1, 1, -1, 1, -1, 1]

t = int(input())
for test_case in range(1, t+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(m)]
    # print(n, m, arr)
    board = [[0]*n for _ in range(n)]
    # 기본 돌 놓기 (1은 흑돌, 2는 백돌).
    board[n//2-1][n//2-1] = 2
    board[n//2][n//2] = 2
    board[n//2-1][n//2] = 1
    board[n//2][n//2-1] = 1
    # print(board)

    # arr for 문으로 돌면서 돌 놓고, 주변도 해당 색상으로 변경하기
    for i in arr:
        row = i[1]-1
        col = i[0]-1
        color = i[2]
        board[row][col] = color
        # 가로, 세로, 대각선 사이에 있는 값 돌 i[2]값으로 바꾸기
        # 가로 검사
        for d in range(8):
            nr, nc = row+dr[d], col+dc[d]
            flip = []
            while 0<=nr<n and 0<=nc<n:
                if board[nr][nc] == 0:
                    break
                if board[nr][nc] == color:
                    for fr, fc in flip:
                        board[fr][fc] = color
                    break
                flip.append((nr, nc))
                nr+=dr[d]
                nc+=dc[d]

        black = sum(i.count(1) for i in board)
        white = sum(i.count(2) for i in board)

    print(f"#{test_case} {black} {white}")