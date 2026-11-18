for _ in range(10):
    test_case = int(input())
    arr = [input() for _ in range(100)]
    max_len = 1
    find = False
    # 회문 길이가 100부터 시작해서 1씩 줄어들면서, 그 갯수에 해당하는 회문 찾으면 (max_len >1 )이면 프로그램 종료
    for l in range(100, 0, -1):
        for i in range(100):
            # 가로 회문 검사
            for col in range(101-l):
                word = arr[i][col:col+l]
                if word == word[::-1]:
                    max_len = l
                    find = True
                    # print(l, i, col, word, find)
                    break
            if find:
                break
            # 세로 회문 검사
            col_slice = ''.join([row[i] for row in arr])
            for j in range(101-l):
                word = col_slice[j:j+l]
                if word == word[::-1]:
                    max_len = l
                    find = True
                    # print(l, i, col, j, word, find)
                    break

        if find:
            break

    print(f"#{test_case} {max_len}")