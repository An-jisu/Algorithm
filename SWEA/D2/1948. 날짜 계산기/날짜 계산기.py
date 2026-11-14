t = int(input())
for test_case in range(1, t+1):
    fm, fd, sm, sd = map(int, input().split())
    d = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    result = 0
    if fm==sm:
        result = sd-fd+1
    else: 
        result+=(d[fm-1]-fd+1)
        for i in range(fm+1, sm+1):
            if i == sm:
                result+=sd
            else:
                result+=d[i-1]
    print(f"#{test_case} {result}")
