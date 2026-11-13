t = int(input())
for test_case in range(1, t+1):
    n = input()
    total = 0
    count = 0
    res = []
    while True:
        if len(res) == 10:
            print(f"#{test_case} {count}")
            break
        count+=int(n)
        total = total+int(n)
        for i in str(total): 
            if int(i) not in res:
                res.append(int(i))