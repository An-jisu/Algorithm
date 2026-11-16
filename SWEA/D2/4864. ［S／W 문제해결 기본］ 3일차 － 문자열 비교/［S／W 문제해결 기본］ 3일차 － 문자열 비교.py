t = int(input())
for test_case in range(1, t+1):
    str1 = input()
    str2 = input()
    result = 0
    #str2 0부터 len(str2)-len(str1) 까지 돌면서 확인
    for i in range(0, len(str2)-len(str1)+1):
        if str2[i:i+len(str1)] == str1:
            result = 1
            break
    print(f"#{test_case} {result}")