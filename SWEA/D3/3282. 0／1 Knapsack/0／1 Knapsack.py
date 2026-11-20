def dfs(idx, w_sum):
    global max_value
    # 종료 조건 (k 값을 넘으면)
    if w_sum > k:
        return -float('inf')
    if idx == n:
        return 0
    if dp[idx][w_sum] != -1:  # 이미 계산한 상태면 바로 반환
        return dp[idx][w_sum]

    pick = dfs(idx+1, w_sum+arr[idx][0])+arr[idx][1]
    skip = dfs(idx+1, w_sum)

    dp[idx][w_sum] = max(pick, skip)
    return dp[idx][w_sum]


t = int(input())
for test_case in range(1, t+1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dp = [[-1]*(k+1) for _ in range(n)]
    # print(n, k, arr)

    print(f"#{test_case} {dfs(0, 0)}")