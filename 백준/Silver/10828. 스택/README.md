# [Silver IV] 스택 - 10828 

[문제 링크](https://www.acmicpc.net/problem/10828) 

### 성능 요약

메모리: 31256 KB, 시간: 48 ms

### 분류

자료 구조, 스택

### 문제 설명

<p>정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.</p>

<p>명령은 총 다섯 가지이다.</p>

<ul>
	<li>push X: 정수 X를 스택에 넣는 연산이다.</li>
	<li>pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.</li>
	<li>size: 스택에 들어있는 정수의 개수를 출력한다.</li>
	<li>empty: 스택이 비어있으면 1, 아니면 0을 출력한다.</li>
	<li>top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.</li>
</ul>

### 입력 

 <p>첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.</p>

### 출력 

 <p>출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.</p>  <br><br>
 
 <hr>

## 👑 나의 풀이: <br>
<code>
#명령의 수 입력받기
n = int(input())
arr = []
#명령의 수 만큼, 명령 입력받기 (for문)- 명령에 따라 스택 함수 호출
for i in range(n):
  a = input()
  if a=='pop':
    if len(arr)==0:
      print(-1)
    else:
      print(arr.pop())
  elif a=='size':
    print(len(arr))
  elif a=='empty':
    if len(arr)==0:
      print(1)
    else:
      print(0)
  elif a=='top':
    if len(arr)==0:
      print(-1)
    else:
      print(arr[-1])
  elif 'push' in a:
    arr.append(a.split()[1])
</code> <br>
-> 나의 처음 코드는 위와 같았다. c언어에서의 스택은 정해진 구조가 존재하지만, 파이썬에서는 존재하지 않는다. 따라서 리스트를 이용하여 구현해주었다. 일단, 명령의 개수를 입력받고, 그 갯수만큼 for문을 통해 반복문 하면서 명령을 입력받았다. 명령에 따라서, 각각의 행동을 수행해주었다. 이렇게 코드를 실행하자, '시간 초과'문제가 생겨났다!!! <br><br>
- input()의 사용으로 시간 초과<br>
- sys.stdin.readline()을 통해 입력받기 <br><br>

## ⭕ 다른 사람의 풀이: <br>
<code>
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
</code> <br><br>

## ✔ What I learned: <br>
-> 스택: 후입선출!! 파이썬에 list pop 함수가 존재함!! 스택<br>
-> 파이썬에서input()을 사용하면, 시간초과 문제가 발생하기 쉬우므로, <b>import sys/ sys.stdin.readline()</b>을 사용하도록 하자! <br>
