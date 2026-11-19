for test_case in range(1, 11):
    n, pwd = input().split()
    answer = []
    for i in pwd:
        if answer and answer[-1] == i:
            answer.pop()
        else:
            answer.append(i)
        # print(answer)
    print(f"#{test_case} {''.join(answer)}")