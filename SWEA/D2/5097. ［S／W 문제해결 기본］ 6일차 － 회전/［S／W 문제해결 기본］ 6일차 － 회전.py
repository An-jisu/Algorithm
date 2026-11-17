t = int(input())
for test_case in range(1, t+1):
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    # m번 돌면서 nums값 업데이트 (nums[1:]+nums[0])
    for i in range(m):
        slicedArr = nums[1:]
        slicedArr.append(nums[0])
        nums = slicedArr

    print(f"#{test_case} {nums[0]}")