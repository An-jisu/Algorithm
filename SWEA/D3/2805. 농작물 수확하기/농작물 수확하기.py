# split은 공백 기준이라 숫자 하나씩 넣고 싶은ㄱ ㅕㅇ우: 벨로그 넣기
t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    arr = [list(map(int, list(input()))) for _ in range(n)]
    # print(arr)
    result = 0
    midIdx = (n -1)//2
    currentStartIdx = midIdx

    for i in range(n):
        # mid >= i 인 경우: 2(i+1)-1개
        if midIdx >= i:
            value = arr[i][currentStartIdx: currentStartIdx+2*(i+1)-1]
            result+= sum(value)
            currentStartIdx = currentStartIdx+1 if midIdx ==i else  currentStartIdx-1
            # print(value, result, currentStartIdx)

        # mid < i 인 경우: 2(n-i)-1
        else:
            value = arr[i][currentStartIdx: currentStartIdx+2*(n-i)-1]
            result+= sum(value)
            currentStartIdx+=1
            # print(value, result, currentStartIdx)
    print(f"#{test_case} {result}")