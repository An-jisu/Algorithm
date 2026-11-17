t = int(input())
for test_case in range(1, t + 1):
    n = input().split()
    arr = []
    for i in range(len(n)):
        #숫자인 경우
        if n[i].isdigit():
            arr.append(int(n[i]))
        else:
            if n[i] == '.':
                if len(arr) == 1:
                    print(f"#{test_case} {arr[0]}")
                else:
                    print(f"#{test_case} error")
                break
            # 숫자가 부족한 경우 에러 출력
            if len(arr) < 2:
                print(f"#{test_case} error")
                break
            b = arr.pop()
            a = arr.pop()
            if n[i] == '+':
                arr.append(a+b)
            elif n[i] == '-':
                arr.append(a-b)
            elif n[i] == '*':
                arr.append(a*b)
            elif n[i] == '/':
                arr.append(a//b)
