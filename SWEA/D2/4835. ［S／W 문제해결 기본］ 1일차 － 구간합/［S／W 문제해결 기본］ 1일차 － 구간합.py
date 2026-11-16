t = int(input())
for test_case in range(1, t+1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    result = []
    for i in range(0,len(arr)-m+1):
        result.append(sum(arr[i:i+m]))
    print(f"#{test_case} {max(result)-min(result)}")