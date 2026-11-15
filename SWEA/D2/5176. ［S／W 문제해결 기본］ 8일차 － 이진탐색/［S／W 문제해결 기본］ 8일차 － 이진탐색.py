def in_order(node):
  global cnt
  if node <= n:  
    in_order(2 * node) 
    arr[node] = cnt
    cnt += 1
    in_order(2 * node + 1)


t = int(input())
for test_case in range(1, t + 1):
  n = int(input())
  cnt = 1
  arr = [0] * (n + 1)

  in_order(1)

  print(f'#{test_case} {arr[1]} {arr[n//2]}')
