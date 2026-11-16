t = int(input())
for test_case in range(1, t+1):
    n = input()
    result = []
    cou = {'}': '{', ')':'('}
    suc = 1
    # 문자하나씩 돌면서 {이거 (이면 result에 넣고, }이거나 )이면은 result의 마지막 값과 비교해서 값이 없거나 다르면 즉시 반복문 빠져나와(1), 같으면 마지막 값 꺼냄. 그렇게 for문 다 돌았는데, result에 값이 남아있으면 suc값 실패로 또 변경. 
    for i in n: 
        if i in ['{', '(']:
            result.append(i)
        elif i in ['}', ')']:
            if len(result)!=0 and cou[i] == result[-1]:
                result.pop()
            else:
                suc = 0
                break
    if len(result) != 0:
        suc = 0

    print(f"#{test_case} {suc}")