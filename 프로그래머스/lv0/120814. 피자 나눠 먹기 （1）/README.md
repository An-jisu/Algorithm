# [level 0] 피자 나눠 먹기 (1) - 120814 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120814?language=javascript) 

### 성능 요약

메모리: 33.4 MB, 시간: 0.04 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

Empty

### 문제 설명

<p>머쓱이네 피자가게는 피자를 일곱 조각으로 잘라 줍니다. 피자를 나눠먹을 사람의 수 <code>n</code>이 주어질 때, 모든 사람이 피자를 한 조각 이상 먹기 위해 필요한 피자의 수를 return 하는 solution 함수를 완성해보세요.</p>

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
<td>7</td>
<td>1</td>
</tr>
<tr>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td>15</td>
<td>3</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>7명이 최소 한 조각씩 먹기 위해서 최소 1판이 필요합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>1명은 최소 한 조각을 먹기 위해 1판이 필요합니다.</li>
</ul>

<p>입출력 예 #3</p>

<ul>
<li>15명이 최소 한 조각씩 먹기 위해서 최소 3판이 필요합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges  <br><br>

<hr>

## 🎁 나의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/415dfe93-6b30-4115-bdb5-a1eb3cf43289) <br>
-> 7, 14..이렇게 피자 조각 수의 배수인 경우에는 그 나눈값을 return 하지만, 그렇지 않은 경우에는 +1한 값을 return해주기 위해 조건문을 써 주었다. <br><br>

## ⭕ 다른 사람의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/db2f0adf-14f3-48bb-a1c0-2a67ea3eb44a) <br>
-> ceil을 통해 내가 한 풀이를 완전 간단하게 처리가능하다. <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/78390d43-f7f8-46c6-aac6-d2bf953839dd) <br>
-> 삼항 연산자로는 이런식으로 나타낼 수 있다. <br><br>

## ✔️ What I learned: <br>
- floor: 작거나 같은 정수 중 가장 큰 정수 return <br>
- ceil: 크거나 같은 정수 중 가장 작은 정수 return <br>
- > 그 의미? 특성을 제대로 알지 못했던 것 같다. 반올림, 반내림이라고 생각해서.5를 기준으로 한다 생각했다. <br>
-> js에서는 if else 조건문 보다는 삼항연산자가 더 많이 쓰인다는 것!! 연습하
