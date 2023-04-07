#개수 입력받기
n = int(input())
turn=0 #2로 나누어떨어지지않으면 상근, 떨어지면 창영
while(1):
  #종료조건 생성 (n==0)
  if n==0:
    break
  #턴 정하기
  turn = (turn+1)%2
  if n<3:
    n-=1
    continue
  else:
    n-=3

#결괏값 출력 (break되면, 그때 turn에 담긴 사람이 승리)
if turn%2==0:
  print("CY")
else:
  print("SK")