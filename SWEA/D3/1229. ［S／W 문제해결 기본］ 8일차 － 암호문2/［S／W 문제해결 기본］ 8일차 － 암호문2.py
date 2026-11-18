for test_case in range(1, 11):
    n = int(input())
    original = input().split()
    cmd_num = int(input())
    cmds = input().replace('I', '|').replace('D', '|').split('| ')[1:]
    # print(n, cmd_num, cmds)

    for cmd in cmds:
        cmd = cmd.split()
        # print(cmd)
        loc = int(cmd[0])
        act_num = int(cmd[1])

        # D 인 경우
        if len(cmd) == 2:
            original = original[:loc] + original[loc+act_num:]

        # I 인 경우
        else:
            nums = cmd[2:]
            original = original[:loc] + nums + original[loc:]

    print(f"#{test_case} {' '.join(original[:10])}")