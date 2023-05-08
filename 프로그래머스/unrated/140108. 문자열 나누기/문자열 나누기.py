#가장 첫번째 글자 x를 기준으로, 그 후로 하나씩 접근하면서, 그 수까지 x와 x가 아닌 수가 같아지면분리
#s의 길이만큼 반복문 돌면서, x정하고(x인 수, x아닌 수 같아지면-변수들 모두 초기화 answer+1)
def solution(s):
    answer = 0
    x = s[0]
    num_x = 0
    num_not_x = 0
    for i in range(0,len(s)-1):
        if s[i]==x:
            num_x+=1
        else:
            num_not_x+=1
        if num_x==num_not_x:
            answer+=1
            x = s[i+1]
            num_x = 0
            num_not_x = 0
    return answer+1