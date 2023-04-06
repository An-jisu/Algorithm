# [level 0] 문자열 밀기 - 120921 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120921) 

### 성능 요약

메모리: 10.1 MB, 시간: 0.01 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

<br/>정확성: 100.0<br/>합계: 100.0 / 100.0

### 문제 설명

<p>문자열 "hello"에서 각 문자를 오른쪽으로 한 칸씩 밀고 마지막 문자는 맨 앞으로 이동시키면 "ohell"이 됩니다. 이것을 문자열을 민다고 정의한다면 문자열 <code>A</code>와 <code>B</code>가 매개변수로 주어질 때, <code>A</code>를 밀어서 <code>B</code>가 될 수 있다면 밀어야 하는 최소 횟수를 return하고 밀어서 <code>B</code>가 될 수 없으면 -1을 return 하도록 solution 함수를 완성해보세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>0 &lt; <code>A</code>의 길이 = <code>B</code>의 길이 &lt; 100</li>
<li><code>A</code>, <code>B</code>는 알파벳 소문자로 이루어져 있습니다.</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>A</th>
<th>B</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>"hello"</td>
<td>"ohell"</td>
<td>1</td>
</tr>
<tr>
<td>"apple"</td>
<td>"elppa"</td>
<td>-1</td>
</tr>
<tr>
<td>"atat"</td>
<td>"tata"</td>
<td>1</td>
</tr>
<tr>
<td>"abc"</td>
<td>"abc"</td>
<td>0</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>"hello"를 오른쪽으로 한 칸 밀면 "ohell"가 됩니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>"apple"은 몇 번을 밀어도 "elppa"가 될 수 없습니다.</li>
</ul>

<p>입출력 예 #3</p>

<ul>
<li>"atat"는 오른쪽으로 한 칸, 세 칸을 밀면 "tata"가 되므로 최소 횟수인 1을 반환합니다.</li>
</ul>

<p>입출력 예 #4</p>

<ul>
<li>"abc"는 밀지 않아도 "abc"이므로 0을 반환합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges <br><br>

<hr>

## 👑 나의 풀이: <br>
![image](https://user-images.githubusercontent.com/70849122/230406812-8bc8260d-fa18-424f-90f7-d80ced423f0f.png)
-> 처음엔 그냥 한번만 밀었을 경우에 A와 B가 같은지를 따지는 문제인 줄 알았다. <br>
-> 둘이 처음부터 같은 경우 0을 return 하게 하였다. <br>
-> for문을 이용하여 길이만큼 밀면서, 만약 같아지면 반복문을 빠져나와 count를 출력하게 하였다. <br>
-> 그런데, count 값이 길이와 같으면, 밀어서 B와 같아질 수 없다는 것이므로 -1을 반환하도록 처리하였다. <br>

## ⭕ 다른 사람의 풀이: <br>
![image](https://user-images.githubusercontent.com/70849122/230419757-0eed1ded-1da9-4d31-b9d8-a3996ea014f8.png) <br>
-> 뒤에 것이 앞당겨지는 것이므로, 앞과 뒤가 연결되어 그 단어를 만들 수 있을 것이다. 그 인덱스는 몇 번 밀었는지를 나타낸다.<br>
![image](https://user-images.githubusercontent.com/70849122/230419847-7fef4833-60e4-416d-a360-bd149fee2a3c.png) <br>
-> 큐를 사용하여, 하나씩 rotate 시키면서, 같아지면 그 cnt를 반환한다. (cnt에는 민 횟수가 들어갈 것이다. 0이면 두개가 완전히 같은 것) for문을 나왔는데도 return이 안되었으면 밀어서 B를 만들 수 없는 것이므로 -1을 반환한다.<br><br>

## ✔ What I learned: <br>
- string.find(찾을문자): 해당 위치의 index 반환<br>
- dequeue.rotate(): 음수-왼쪽회전/양수-오른쪽 회전<br>
![image](https://user-images.githubusercontent.com/70849122/230423657-4d01a8c9-c734-46fa-97f1-20423d280e25.png) <br>
-> 오른쪽 회전하면 뒤의 수가 앞으로 옴 
