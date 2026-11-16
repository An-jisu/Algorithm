def dfs(row, now_sum):
    global min_sum
    
    # 현재까지의 합이 이미 최소값보다 크거나 같다면 더 탐색할 필요 없음 (가지치기)
    if now_sum >= min_sum:
        return
    
    # 마지막 행까지 탐색을 마쳤을 경우 최소값 갱신
    if row == N:
        min_sum = min(min_sum, now_sum)
        return
    
    for col in range(N):
        if not visited[col]:
            visited[col] = True
            dfs(row + 1, now_sum + arr[row][col])
            visited[col] = False  # 원상복구 (백트래킹)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    visited = [False] * N
    min_sum = float('inf')  # 충분히 큰 값으로 초기화
    
    dfs(0, 0)
    print(f"#{tc} {min_sum}")
