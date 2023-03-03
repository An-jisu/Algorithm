def solution(numbers, direction):
    if direction=="right":
        #저장
        num = numbers[len(numbers)-1]
        print(num)
        #당겨
        for i in range(len(numbers)-1, 0, -1):
            numbers[i] = numbers[i-1]
        #삽입
        numbers[0] = num
    else:
        num = numbers[0]
        for i in range(0, len(numbers)-1):
            numbers[i] = numbers[i+1]
        numbers[len(numbers)-1] = num   
    return numbers