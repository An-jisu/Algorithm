t = int(input())
for test_case in range(1, t+1):
    word = input().strip()
    result = 0
    if word == word[::-1]:
        result = 1
    print(f"#{test_case} {result}")