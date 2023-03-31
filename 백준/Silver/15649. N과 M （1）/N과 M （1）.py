#1부터 n까지의 자연수, 각 수열은 m개의 요소
n, m = map(int, input().split())
ans = []

def back():
  if (len(ans) == m):
    print(' '.join(map(str, ans)))
    return
  for i in range(1, n + 1):
    if i not in ans:
      ans.append(i)
      back()
      ans.pop()

back()