# [level 0] 저주의 숫자 3 - 120871 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120871) 

### 성능 요약

메모리: 10.3 MB, 시간: 0.03 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

<br/>정확성: 100.0<br/>합계: 100.0 / 100.0

### 문제 설명

<p>3x 마을 사람들은 3을 저주의 숫자라고 생각하기 때문에 3의 배수와 숫자 3을 사용하지 않습니다. 3x 마을 사람들의 숫자는 다음과 같습니다.</p>
<table class="table">
        <thead><tr>
<th>10진법</th>
<th>3x 마을에서 쓰는 숫자</th>
<th>10진법</th>
<th>3x 마을에서 쓰는 숫자</th>
</tr>
</thead>
        <tbody><tr>
<td>1</td>
<td>1</td>
<td>6</td>
<td>8</td>
</tr>
<tr>
<td>2</td>
<td>2</td>
<td>7</td>
<td>10</td>
</tr>
<tr>
<td>3</td>
<td>4</td>
<td>8</td>
<td>11</td>
</tr>
<tr>
<td>4</td>
<td>5</td>
<td>9</td>
<td>14</td>
</tr>
<tr>
<td>5</td>
<td>7</td>
<td>10</td>
<td>16</td>
</tr>
</tbody>
      </table>
<p>정수 <code>n</code>이 매개변수로 주어질 때, <code>n</code>을 3x 마을에서 사용하는 숫자로 바꿔 return하도록 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>n</code> ≤ 100</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>n</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>15</td>
<td>25</td>
</tr>
<tr>
<td>40</td>
<td>76</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>15를 3x 마을의 숫자로 변환하면 25입니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>40을 3x 마을의 숫자로 변환하면 76입니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges  <br><br>

<hr>

## 👑 나의 풀이: <br>
![image](https://user-images.githubusercontent.com/70849122/228250008-c3d45eb4-e47d-4363-9f07-1706b885358c.png)
-> 처음에는 결괏값들에 대한 규칙을 찾아내려고 하였다. 하지만, 규칙이 존재하지 않았다. 그래서... 결괏값들을 배열 안에 넣어놓고, 그에 맞는 인덱스를 반환해주는 방식으로 코드를 짰다. 그런데!! 런타임 에러가 나는 것이다. 반복문을 너무 큰 크기로 반복했거나 많은 리스트나 변수들을 사용해서 저장 메모리가 초과되었을 수도 있을 것 같다. <br><br>

## ⭕ 다른 사람의 풀이: <br>
![image](https://user-images.githubusercontent.com/70849122/228252378-aeae5029-32e8-49de-b3a8-c8ff62872b48.png) <br>
-> 그냥, n만큼 반복문을 돌면서 만약 3의배수이거나, 3을 포함하고 있으면, 반복문을 다음으로 넘어가지 않고 1을 더 더하도록 코드를 짰다... 이렇게 간단할 수가 
 <br><br>
