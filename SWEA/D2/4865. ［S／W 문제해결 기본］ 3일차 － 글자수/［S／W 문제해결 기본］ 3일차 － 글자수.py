t = int(input())
for test_case in range(1, t+1):
    str1 = input()
    str2 = input()
    count = {}
    # str1의 값을 하나씩 돌면서, 딕셔너리 요소 만들고, str2값 하나씩 돌면서 그 값 증가시키고, max값 출력
    for i in str1:
        if i not in count:
            count[i]=0

    for i in str2:
        if i in count:
            count[i]+=1
    
    print(f"#{test_case} {max(count.values())}")