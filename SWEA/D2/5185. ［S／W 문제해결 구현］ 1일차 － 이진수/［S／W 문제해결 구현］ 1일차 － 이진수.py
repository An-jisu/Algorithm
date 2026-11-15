t = int(input())
for test_case in range(1, t+1):
    n, word = input().split()
    result = ''
    for w in word:
        changed = str(bin(int(w, 16)))[2:]
        if len(changed) < 4: 
            changed = '0'*(4-len(changed)) + changed
        result+=changed

    print(f"#{test_case} {result}")