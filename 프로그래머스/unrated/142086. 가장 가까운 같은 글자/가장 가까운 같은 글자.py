#첫번째 문자부터 접근하면서,앞에 자기 자신과 같은 문자가 있으면 얼마나 앞에 있는지 표현
def solution(s):
    #1번째는 -1로 초기화
    answer = [-1]
    #반복문 돌면서(1,len(s)까지)-그 수부터 처음까지 반복문 돌면서, 있으면 그 인덱스와 i의 차이 저장-> append(0이면, 앞에 없는 것이므로 -1append)
    for i in range(1, len(s)):
        num = 0
        for j in range(i-1,-1, -1):
            if s[i]==s[j]:
                num = i-j
                break
        if num==0:
            answer.append(-1)
        else:
            answer.append(num)
    return answer