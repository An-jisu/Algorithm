def solution(s):
    #공백을 기준으로 나눠서 배열에 넣기
    answer = []
    answer = s.split(' ')
    sum = 0
    
    #z가 아니면 int로 바꿔서 다 더하기(z면 그 전꺼 빼기)-배열의 길이 만큼 실행
    for i in range(len(answer)):
        if(answer[i]!='Z'):
            sum+=int(answer[i])
        else:
            sum-=int(answer[i-1])
    
    return sum