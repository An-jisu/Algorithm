# [Silver III] 문자열 집합 - 14425 

[문제 링크](https://www.acmicpc.net/problem/14425) 

### 성능 요약

메모리: 36688 KB, 시간: 116 ms

### 분류

자료 구조, 문자열, 해시를 사용한 집합과 맵, 트리를 사용한 집합과 맵

### 문제 설명

<p>총 N개의 문자열로 이루어진 집합 S가 주어진다.</p>

<p>입력으로 주어지는 M개의 문자열 중에서 집합 S에 포함되어 있는 것이 총 몇 개인지 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 문자열의 개수 N과 M (1 ≤ N ≤ 10,000, 1 ≤ M ≤ 10,000)이 주어진다. </p>

<p>다음 N개의 줄에는 집합 S에 포함되어 있는 문자열들이 주어진다.</p>

<p>다음 M개의 줄에는 검사해야 하는 문자열들이 주어진다.</p>

<p>입력으로 주어지는 문자열은 알파벳 소문자로만 이루어져 있으며, 길이는 500을 넘지 않는다. 집합 S에 같은 문자열이 여러 번 주어지는 경우는 없다.</p>

### 출력 

 <p>첫째 줄에 M개의 문자열 중에 총 몇 개가 집합 S에 포함되어 있는지 출력한다.</p> <br><br>
 
 <hr>
 
## 👑 나의 풀이: <br>
<code>
#집합의 문자열 수, 검사할 문자열 수 입력받기
N, M = map(int, input().split())
count = 0

#리스트 2개 생성하여, 각각 수 만큼 for문 돌면서 append 시키기
N_arr = []
M_arr = []
for i in range(N):
  N_arr.append(input())
for i in range(M):
  M_arr.append(input())
print(N_arr)
print(M_arr)
#검사할 문자열 수 만큼 반복문 돌면서, 만약 집합에 포함되면 count
for i in M_arr:
  if i in N_arr:
    count+=1

#결괏값 출력
print(count)
</code><br>
-> 일단 n,m을 각각 입력받았다. 그 후, 입력받으며 각각을 리스트를 만들어 입력받으면서 저장하고, M의 크기만큼 반복문을 돌면서, 만약 N집합에 존재하면 count하게 하였고, 그 값을 최종적으로 출력하였다. 결과는 제대로 출력이 되었다. <br>
-> 그런데, 출력초과가 뜨는 것이다...리스트나 반복문이 용량을 많이 잡아먹었나? 그래서 다른 사람들은 어떻게 풀었는지 풀이를 검색해보았다. <br><br>

## ⭕ 다른 사람의 풀이: <br>
<code>
N, M = map(int, input().split())
S = set()
for i in range(N):
    S.add(input())
ans = 0
for _ in range(M):
    t = input()
    if t in S:
        ans+=1
print(ans)
</code><br>
-> list를 써서 시간초과가 나왔고, set을 사용하여 풀이를 한 것이다. t가 S에 있는지 확인할 때, in을 사용했는데 자료 구조에 따라 시간 복잡도가 다른 것이다. set은 key를 통해 접근을 하기 때문에, 빠르다. 그리고, set에 data를 추가할 때는 add함수를 사용해준다!! <br><br>

## ✔ What I learned: <br> 
-> list보다는 set 자료형이 자료들에 접근할 때 더 빠르다는 것! <br><br>
