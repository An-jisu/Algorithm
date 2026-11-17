for _ in range(1, 11):
    test_case = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    right = []
    left = []
    result = []
    for i in range(100):
        # 행의 합
        result.append(sum(arr[i]))
        # 열의 합
        result.append(sum([row[i] for row in arr]))
        # 오른쪽 아래 대각선 값들의 집합
        right.append(arr[i][i])
        # 왼쪽 아래 대각선 값들의 집합
        left.append(arr[i][4-i])

    # 각 대각선 합도 result에
    result.append(sum(right))
    result.append(sum(left))
    
    print(f"#{test_case} {max(result)}")