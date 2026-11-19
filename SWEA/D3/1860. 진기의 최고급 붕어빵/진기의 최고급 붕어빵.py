t = int(input())
for test_case in range(1, t+1):
    n, m, k = map(int, input().split())
    people = sorted(list(map(int, input().split())))
    # print(n, m, k, people)
    sold = 0
    result = 0

    for i in people:
        # i에서의 현재 붕어빵 갯수 세기 (2초 2개-> 57초? (57//2) 28 *2-> 56개
        remain = (i//m) * k - sold
        if remain == 0:
            result = 0
            break
        else:
            sold +=1
            result = 1
    print(f"#{test_case} {'Possible' if result != 0 else 'Impossible'}")