for test_case in range(1, 11):
    n = int(input())
    nums = list(map(int, input().split()))
    #n번 돌면서, max인 값 1빼고 min의 값 1 더해
    for i in range(n):
        # print(nums[nums.index(max(nums))], nums[nums.index(min(nums))])
        nums[nums.index(max(nums))] -=1
        nums[nums.index(min(nums))] += 1

    print(f"#{test_case} {max(nums)-min(nums)}")