def solution(answers):
    answer = [0, 0, 0]
    s1 = "12345"
    s2 = "21232425"
    s3 = "3311224455"
    #맞힌 문제의 수 저장(answer배열에, 인덱스 순서대로 1,2,3번 학생)
    for i in range(len(answers)):
        if answers[i]==int(s1[i%5]): 
            answer[0]+=1
        if answers[i]==int(s2[i%8]):
            answer[1]+=1
        if answers[i]==int(s3[i%10]):
            answer[2]+=1
    #가장 많은 문제 맞힌 사람 반환
    if answer.count(max(answer))>1:
        return [i+1 for i in range(3) if answer[i]==max(answer)]
            
                
    else:
        return [answer.index(max(answer))+1]