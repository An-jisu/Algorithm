for test_case in range(1, 11):
    n = int(input())
    original = input().split()
    com_num = int(input())
    coms = input().split('I ')[1:]
    # print(n, original, com_num, coms)

    for com in coms:
        com = com.split()
        loc = int(com[0].strip())
        num = int(com[1])
        nums = com[2:]
        # print(com, loc, num, nums)

        # 추가
        original = original[:loc] + nums + original[loc:]
        # print(original)
    # print(original)
    print(f"#{test_case} {' '.join(original[:10])}")