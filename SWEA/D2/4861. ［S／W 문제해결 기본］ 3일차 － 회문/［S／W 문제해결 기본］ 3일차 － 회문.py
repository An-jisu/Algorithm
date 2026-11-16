t = int(input())
for test_case in range(1, t+1):
    n, m = map(int, input().split())
    arr = [input() for i in range(n)]
    find=''
    # 가로 회문 찾기 (n만큼 반복문 돌면서, 그 안에서 또 0부터 n-m까지 돌면서 회문인거 찾기)
    for i in range(n):
        for j in range(0, n-m+1):
            if arr[i][j:j+m] == arr[i][j:j+m][::-1]:
                find=arr[i][j:j+m]
                break
        if len(find)>0:
            break

    # 세로 회문 찾기 (n만큼 반복문 돌면서, 열 가져와서 배열로 만들고 또 그 안에서 n-m만큼 돌면서 회문 있는지 찾기)
    if len(find)==0:
        for i in range(n):
            col_slice = [col[i] for col in arr]
            for j in range(0, n-m+1):
                if col_slice[j:j+m] == col_slice[j:j+m][::-1]:
                    find=''.join(col_slice[j:j+m])
                    break
            if len(find)>0:
                break
    print(f"#{test_case} {find}")