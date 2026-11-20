tc = int(input())
for test_case in range(1, tc+1):
    n = int(input())
    nums = list(map(int, input().split()))
    # print(n, nums)
    result = []

    # 1이 가장 먼저 나타나는 요일(인덱스)부터 시작해서 while문 돌면서 result값 업데이트 (마지막요일이면 다시 앞으로)
    # 현재까지 들은 일 수 업데이트 하다가 (목표 달성하면 종료)
    # -> 안돼!! 그냥 각 1인 것에 시작하는 것만큼 반복하면서 최솟값 구하자.

    for i in range(7):
        if nums[i] == 1:
            index = i
            total = 0
            currentGoal = 0
            while currentGoal < n:
                if nums[index] == 1:
                    currentGoal+=1
                total+=1
                index = (index+1)%7
            result.append(total)
            # print(nums, i, total, result)

    print(f"#{test_case} {min(result)}")