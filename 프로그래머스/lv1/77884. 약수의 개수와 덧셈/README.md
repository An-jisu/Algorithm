# [level 1] 약수의 개수와 덧셈 - 77884 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/77884) 

### 성능 요약

메모리: 10.1 MB, 시간: 0.35 ms

### 구분

코딩테스트 연습 > 월간 코드 챌린지 시즌2

### 채점결과

Empty

### 문제 설명

<p>두 정수 <code>left</code>와 <code>right</code>가 매개변수로 주어집니다. <code>left</code>부터 <code>right</code>까지의 모든 수들 중에서, 약수의 개수가 짝수인 수는 더하고, 약수의 개수가 홀수인 수는 뺀 수를 return 하도록 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>left</code> ≤ <code>right</code> ≤ 1,000</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>left</th>
<th>right</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>13</td>
<td>17</td>
<td>43</td>
</tr>
<tr>
<td>24</td>
<td>27</td>
<td>52</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p><strong>입출력 예 #1</strong></p>

<ul>
<li>다음 표는 13부터 17까지의 수들의 약수를 모두 나타낸 것입니다.</li>
</ul>
<table class="table">
        <thead><tr>
<th>수</th>
<th>약수</th>
<th>약수의 개수</th>
</tr>
</thead>
        <tbody><tr>
<td>13</td>
<td>1, 13</td>
<td>2</td>
</tr>
<tr>
<td>14</td>
<td>1, 2, 7, 14</td>
<td>4</td>
</tr>
<tr>
<td>15</td>
<td>1, 3, 5, 15</td>
<td>4</td>
</tr>
<tr>
<td>16</td>
<td>1, 2, 4, 8, 16</td>
<td>5</td>
</tr>
<tr>
<td>17</td>
<td>1, 17</td>
<td>2</td>
</tr>
</tbody>
      </table>
<ul>
<li>따라서, 13 + 14 + 15 - 16 + 17 = 43을 return 해야 합니다.</li>
</ul>

<p><strong>입출력 예 #2</strong></p>

<ul>
<li>다음 표는 24부터 27까지의 수들의 약수를 모두 나타낸 것입니다.</li>
</ul>
<table class="table">
        <thead><tr>
<th>수</th>
<th>약수</th>
<th>약수의 개수</th>
</tr>
</thead>
        <tbody><tr>
<td>24</td>
<td>1, 2, 3, 4, 6, 8, 12, 24</td>
<td>8</td>
</tr>
<tr>
<td>25</td>
<td>1, 5, 25</td>
<td>3</td>
</tr>
<tr>
<td>26</td>
<td>1, 2, 13, 26</td>
<td>4</td>
</tr>
<tr>
<td>27</td>
<td>1, 3, 9, 27</td>
<td>4</td>
</tr>
</tbody>
      </table>
<ul>
<li>따라서, 24 - 25 + 26 + 27 = 52를 return 해야 합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges  <br><br>

<hr>

## ❤️ 요구 분석과 설계: <br>
-> left와 right가 주어졌을 때, 그 사이의 숫자들의 약수의 갯수를 모두 조사해서, 짝수 개이면 answer에 더하고, 홀수이면 answer에서 빼 주었다. <br><br>
                                                                                                   
## 😀 나의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/faf63595-7117-4c0d-910c-7acafb0bd000) <br>
-> 약수의 개수를 0.5배해서, 나누어떨어지면 짝꿍을 이루므로 2를 더해주었고, 마지막 값을 제곱한 것이 i와 같으면 1을 더해주었다. 약수를 저렇게 구하지 않으면, 너무 많은 값을 조사해서 시간 초과가 뜬다. <br><br>

## ⭕ 다른 사람의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/709a0b28-19a4-4cf7-9af1-7ac3901fd763) <br>
-> 아...나의 풀이에 따르면, 제곱수 인 경우에는 1을 더 더해주고, 그 외의 경우에는 계속 2를 더해준다. 따라서 제곱수인 경우에만, 약수의 개수가 짝수개이다. !!! 이 특징을 이용하면, 더 간단하게 풀 수 있었던 문제이다. 제곱근을 구한 값이, 그것을 int로 바꿔주었을 때와 같으면, 제곱수이다. <br><br>

## ✔️ What I learned: <br>
-> 약수 구하는 코드 그냥 외우기!!!!! <br><br>
