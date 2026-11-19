# 0번부터 그리고 그 뒤의 값들중 하나 그렇게 2개를 선택해서 바꾸고 거기서 또 횟수만큼 바꾼 것들로 최댓값 구하기
def dfs(cnt, nums, k, visited):
    current_str = ''.join(nums)

    # 중복 제거 및 방문 기록 남기기
    if (current_str, cnt) in visited:
        return
    visited.add((current_str, cnt))

    # 종료 조건
    if cnt == k:
        return int(current_str)

    # max 값 구하기
    max_val = 0
    n = len(nums)
    for i in range(n-1):
        for j in range(i+1, n):
            nums[i], nums[j] = nums[j], nums[i]
            result = dfs(cnt+1, nums, k, visited)
            if result is not None and result>max_val:
                max_val=result
            nums[i], nums[j] = nums[j], nums[i]

    return max_val


t = int(input())
for test_case in range(1, t+1):
    num, change_count = input().split()
    nums = list(num)
    k = int(change_count)
    # print(num, change_count)

    visited=set()
    ans = dfs(0, nums, k, visited)

    print(f"#{test_case} {ans}")