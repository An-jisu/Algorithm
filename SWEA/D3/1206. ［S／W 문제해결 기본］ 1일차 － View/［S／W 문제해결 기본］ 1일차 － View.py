for test_case in range(1, 11):
    n = int(input())
    heights = list(map(int, input().split()))
    # print(heights)
    result = 0
    # height, 앞 뒤 2개씩 보았을 때 모두 height 보다 작다면 (앞 뒤 4개의 최댓값과 height값과의 차이 더함)
    for i in range(2, len(heights)-2):
        # print(max(heights[i-2:i], heights[i+1:i+3]), heights[i])
        if max(heights[i-2:i]+heights[i+1:i+3]) < heights[i]:
            result+=(heights[i]-max(heights[i-2:i]+heights[i+1:i+3]))

    print(f"#{test_case} {result}")