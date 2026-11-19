def dfs(i, current_sum):
    global count
    if current_sum == k:
        count+=1
        return
    if i == n or current_sum > k:
        return

    dfs(i+1, current_sum+arr[i])
    dfs(i+1, current_sum)

t = int(input())
for test_case in range(1, t+1):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    count = 0

    dfs(0, 0)

    print(f"#{test_case} {count}")