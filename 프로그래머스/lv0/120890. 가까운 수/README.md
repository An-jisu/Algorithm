# [level 0] 가까운 수 - 120890 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120890#) 

### 성능 요약

메모리: 10.1 MB, 시간: 0.01 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

<br/>정확성: 100.0<br/>합계: 100.0 / 100.0

### 문제 설명

<p>정수 배열 <code>array</code>와 정수 <code>n</code>이 매개변수로 주어질 때, <code>array</code>에 들어있는 정수 중 <code>n</code>과 가장 가까운 수를 return 하도록 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>array</code>의 길이 ≤ 100</li>
<li>1 ≤ <code>array</code>의 원소 ≤ 100</li>
<li>1 ≤ <code>n</code> ≤ 100</li>
<li>가장 가까운 수가 여러 개일 경우 더 작은 수를 return 합니다.</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>array</th>
<th>n</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>[3, 10, 28]</td>
<td>20</td>
<td>28</td>
</tr>
<tr>
<td>[10, 11, 12]</td>
<td>13</td>
<td>12</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>3, 10, 28 중 20과 가장 가까운 수는 28입니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>10, 11, 12 중 13과 가장 가까운 수는 12입니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges  <br><br>

<hr>

## 👑 나의 풀이:<br>
: 나는 배열의 요소들에 하나씩 접근하면서 그 차이의 절댓값을 새로운 배열에 넣었다. 그리고 그 배열에서의 최솟값을 구해서, 그 인덱스에 해당하는 값을 return 하였다. 난 처음에는 조건을 놓쳐서, 절댓값이 같은 수가 여러개 일수도 있을 것이라는 생각을 못했다. 하지만 sort()를 하지 않았을 경우에는 한가지 테스트케이스에 대해서 동작이 되지 않았다. 하지만 아직까지 그 이유를 모르겠어....... 반례를 찾을 수 없어...<br>

## ⭕ 다른 사람의 풀이: <br>
![image](https://user-images.githubusercontent.com/70849122/223652892-af5a2e81-6f86-4774-881a-fea9c386bf72.png) <br>
-> 와 어떻게 이렇게 풀지.. lamda함수 사용하는 거 연습하자!!
