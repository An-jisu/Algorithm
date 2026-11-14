t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    contents = [input().split() for _ in range(n)]
    result = ['']
    idx = 0
    for i in contents:
        for j in range(int(i[1])):
            result[idx]+=i[0]
            if len(result[idx]) == 10:
                result.append('')
                idx +=1
    
    print(f"#{test_case}")
    for i in result:
        print(i)
