t = int(input())
for test_case in range(1, t+1):
    n = int(input().strip())
    remain = n
    result = [[50000, 0], [10000, 0], [5000, 0], [1000, 0], [500, 0], [100, 0], [50, 0], [10, 0]]
    for i in range(len(result)):                
        result[i][1] = remain // result[i][0]
        remain = remain % result[i][0]

    print(f"#{test_case}")
    print(' '.join([str(x[1]) for x in result]))