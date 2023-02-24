def solution(age):
    a = ['a','b','c','d','e','f','g','h','i','j']
    b = len(str(age))
    answer = []
    for i in range(b):
        answer.insert(0, a[age%10])
        age = age//10
    return ''.join(answer)
    