import sys
#명령의 수 입력받기
n = int(sys.stdin.readline())
arr = []
#명령의 수 만큼, 명령 입력받기 (for문)- 명령에 따라 스택 함수 호출
for i in range(n):
  a = sys.stdin.readline().split()
  order = a[0]
  if order=='pop':
    if len(arr)==0:
      print(-1)
    else:
      print(arr.pop())
  elif order=='size':
    print(len(arr))
  elif order=='empty':
    if len(arr)==0:
      print(1)
    else:
      print(0)
  elif order=='top':
    if len(arr)==0:
      print(-1)
    else:
      print(arr[-1])
  elif order=='push':
    arr.append(a[1])