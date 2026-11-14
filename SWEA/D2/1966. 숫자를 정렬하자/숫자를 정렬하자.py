t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    nums = sorted(list(map(int, input().split())))
    print(f"#{test_case} {' '.join(map(str, nums))}")