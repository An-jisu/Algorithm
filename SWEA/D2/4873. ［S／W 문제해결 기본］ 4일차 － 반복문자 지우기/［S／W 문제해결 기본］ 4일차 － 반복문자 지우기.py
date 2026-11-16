t = int(input())
for test_case in range(1, t+1):
    n = input()
    while len(n) > 0:
        removed = False
        #print('current: '+n)
        for i in range(1, len(n)):
            if n[i] == n[i-1]:
                n = n[0:i-1]+n[i+1:]
                #print(n)
                removed = True
                break
        if not removed:
            break
    print(f"#{test_case} {len(n)}")