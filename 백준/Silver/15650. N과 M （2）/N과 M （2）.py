#1부터 n까지의 자연수, 각 수열은 m개의 요소
n, m = map(int, input().split())
ans = []

def back(a):
  if (len(ans) == m):
    print(' '.join(map(str, ans)))
    return
  for i in range(a+1, n + 1):
      ans.append(i)
      back(i)
      ans.pop()

back(0)