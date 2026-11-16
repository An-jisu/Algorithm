t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    cards = input()
    result = [0]*10
    max_num, max_value = 0, 0
    for card in cards:
        result[int(card)]+=1
    for i in range(0, 10):
        if max_num < result[i]:
            max_num = result[i]
            max_value = i
        elif max_num == result[i]:
            max_value = max(max_value, i)
        else:
            continue
    print(f"#{test_case} {max_value} {max_num}")