t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    nums = list(map(int, input().split()))

    print(f"#{test_case} {max(nums)-min(nums)}")