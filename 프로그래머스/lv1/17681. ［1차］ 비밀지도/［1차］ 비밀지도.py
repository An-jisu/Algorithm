def solution(n, arr1, arr2):
    answer = []
    a1 = []
    a2 = []
    #arr1, arr2를 각각 이진수 변환하여 문자열 저장
    for i,j in zip(arr1,arr2):
        a1.append(format(i, 'b').zfill(n))
        a2.append(format(j, 'b').zfill(n))
    #n만큼 중첩 반복문으로 돌면서 둘 다 0이면 공백/나머지에는 벽(#)으로 answer 채워서 반환
    for i,j in zip(a1, a2):
        temp=''
        for k in range(n):
            if i[k]=='0' and j[k]=='0':
                temp+=' '
            else:
                temp+='#'
        answer.append(temp)
    return answer