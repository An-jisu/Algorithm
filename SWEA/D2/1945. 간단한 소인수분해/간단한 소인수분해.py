t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    arr = [2,3,5,7,11]
    result = [0]*5
    for i in range(len(arr)):
        while True:
            if n%arr[i] !=0: break
            n = n//arr[i]
            result[i]+=1
    print(f"#{test_case} {' '.join(map(str, result))}")