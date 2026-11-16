t = int(input())
for test_case in range(1, t+1):
    n = float(input())
    s = ''
    while n>0:
        n*=2
        s+=str(int(n))
        n-=int(n)

    if(len(s)>12):
        print(f"#{test_case} overflow")
    else:
        print(f"#{test_case} {s}")