for _ in range(10):
    test_case = int(input())
    nums = list(map(int, input().split()))
    # print(nums)

    # result의 마지막값이 0보다 큰 동안 계속 진행
    while nums[-1] > 0:
        for i in range(1, 6):
            new_num = nums.pop(0)-i
            if new_num <= 0:
                nums.append(0)
                break
            else:
                nums.append(new_num)

    print(f"#{test_case} {' '.join([str(i) for i in nums])}")