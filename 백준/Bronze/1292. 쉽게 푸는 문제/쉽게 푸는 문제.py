#문자열 형태로 수열 정의
a,b=map(int,input().split())
data=[]
for i in range(1,b+1):
  for j in range(i):
    data.append(i)

#입력에 따라서 int로 형 변환하여 합을 출력
print(sum(data[a-1:b]))