t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    result = 0
    currentSpeed = 0
    for i in range(n):
        cmd = list(map(int, input().split()))
        if cmd[0] == 1 :
            currentSpeed += cmd[1]
        elif cmd[0] == 2:
            currentSpeed = max(0, currentSpeed-cmd[1])

        result += currentSpeed
    print(f"#{test_case} {result}")