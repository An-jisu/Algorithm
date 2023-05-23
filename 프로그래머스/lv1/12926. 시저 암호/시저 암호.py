def solution(s, n):
    answer = ''
    for i in s:
        if i==' ':
            answer+=i
            continue
        a = chr(ord(i)+n)
        if a>'z':
            a = chr(ord(a)-26)
        if a>'Z' and i.isupper():
            a = chr(ord(a)-26)
        answer+= a
    return answer