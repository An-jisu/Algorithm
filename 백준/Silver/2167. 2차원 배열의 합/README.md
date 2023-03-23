# [Silver V] 2차원 배열의 합 - 2167 

[문제 링크](https://www.acmicpc.net/problem/2167) 

### 성능 요약

메모리: 37032 KB, 시간: 1004 ms

### 분류

구현, 누적 합

### 문제 설명

<p>2차원 배열이 주어졌을 때 (i, j) 위치부터 (x, y) 위치까지에 저장되어 있는 수들의 합을 구하는 프로그램을 작성하시오. 배열의 (i, j) 위치는 i행 j열을 나타낸다.</p>

### 입력 

 <p>첫째 줄에 배열의 크기 N, M(1 ≤ N, M ≤ 300)이 주어진다. 다음 N개의 줄에는 M개의 정수로 배열이 주어진다. 배열에 포함되어 있는 수는 절댓값이 10,000보다 작거나 같은 정수이다. 그 다음 줄에는 합을 구할 부분의 개수 K(1 ≤ K ≤ 10,000)가 주어진다. 다음 K개의 줄에는 네 개의 정수로 i, j, x, y가 주어진다(1 ≤ i ≤ x ≤ N, 1 ≤ j ≤ y ≤ M).</p>

### 출력 

 <p>K개의 줄에 순서대로 배열의 합을 출력한다. 배열의 합은 2<sup>31</sup>-1보다 작거나 같다.</p>

<hr>

## 👑 나의 풀이: <br>
<code>
#배열의 크기 입력받기
a,b = map(int, input().split())
arr = [[0 for j in range(b)] for i in range(a)]

#배열 입력받기
for i in range(a):
  arr[i] = input().split()
print(arr) 
    
#합을 구할 부분의 개수 구하기
num = int(input())

sum_arr = []
#4개의 정수 입력받기
for n in range(num):
  sum = 0
  i,j,x,y = map(int, input().split())
  for u in range(i-1, x):
    for v in range(j-1, y):
      sum+=int(arr[u][v])
  sum_arr.append(str(sum))

for n in range(0, len(sum_arr)):
  print(sum_arr[n])
</code><br>
-> <br><br>

## ⭕ 최종 풀이: <br>
<code>

</code>

## ✔ What I learned: <br>
