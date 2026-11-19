t = int(input())
for test_case in range(1, t+1):
    n, m = map(int, input().split())
    arr = [input() for _ in range(n)]
    cod = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4, '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}
    # print(n, m, arr)
    result = 0
    # 반복문으로 arr 한 줄 씩 돌면서 1을 포함한 경우 암호화 줄 검사 시작, 검사 후 break하여 반복문 빠져나옴
    # 반복문 내에서: 암호화줄에서 뒤에서 오면서 1을 처음으로 만날 때의 1 인덱스 그리고 그 앞의 56개 값 가져와서
    # 7개씩 끊어서 올바른 암호인지 검사 후 결과 출력
    for sen in arr:
        # 암호화 문장 추출
        if '1' in sen:
            # print(sen)
            pwd = []
            # 한 줄에서 암호화 문장 추출
            for i in range(m-1, -1, -1):
                if sen[i] == '1':
                    pwd = sen[i-55:i+1]
                    # print(m, i, sen[i-55:i+1])
                    break

            decoded = [cod[pwd[digit:digit + 7]] for digit in range(0, 50, 7)]
            # print(pwd, decoded)

            # 올바른 암호인지 검사
            total = 0
            for idx, d in enumerate(decoded):
                if idx % 2 ==0:
                    total += (d*3)
                else:
                    total+=d

            if total % 10 ==0:
                result = sum(decoded)
            else:
                result = 0

            # 해당 암호화 문장 검사 이후 빠져나옴
            break
        else:
            continue

    print(f"#{test_case} {result}")