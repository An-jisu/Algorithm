t = int(input())
for test_case in range(1, t+1):
    sen = input().strip()
    # 0~10 마디 갯수 for 문 돌면서 첫 번째 마디, 두 번째 마디 같은지 검사
    for i in range(1, 11): # i가 마디 길이
        if sen[0:i] == sen[i:i+i]:
            print(f"#{test_case} {i}")
            break