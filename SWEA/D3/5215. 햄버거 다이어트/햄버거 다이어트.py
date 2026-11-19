def dfs(idx, s_sum, k_sum):
    global max_value
    # 종료 조건 (칼로리를 넘어가면)
    if k_sum > l:
        return
    # 최댓값 업데이트
    if s_sum > max_value:
        max_value = s_sum
    if idx ==n:
        return

    dfs(idx+1, s_sum+burgers[idx][0], k_sum+ burgers[idx][1])
    dfs(idx + 1, s_sum, k_sum)

t = int(input())
for test_case in range(1, t+1):
    n, l = map(int, input().split())
    burgers = [list(map(int, input().split())) for i in range(n)]
    # print(n, l, burgers)
    max_value = 0
    # 칼로리가 넘지 않게 재료 고르면서 재료에 대한 점수 업데이트
    dfs(0, 0, 0)

    print(f"#{test_case} {max_value}")