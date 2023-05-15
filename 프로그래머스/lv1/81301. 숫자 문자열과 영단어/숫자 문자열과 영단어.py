def solution(s):
    #각 영어에 해당하는 숫자 딕셔너리로 
    num = {"zero": '0', "one": '1', "two": '2', "three": '3', "four": '4', "five": '5', "six": '6',"seven": '7', "eight": '8', "nine": '9'}
    #num만큼 반복하면서, 그 키 값이 s에 존재하면 replace
    for i in num.keys():
        if i in s:
            s = s.replace(i, num[i])
    return int(s)