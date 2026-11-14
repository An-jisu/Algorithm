t = int(input())
for test_case in range(1, t+1):
    nums = sorted(list(map(int, input().split())))
    print(f"#{test_case} {round(sum(nums[i] for i in range(1,len(nums)-1))/8)}") 