# [level 0] 배열 자르기 - 120833 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120833?language=javascript) 

### 성능 요약

메모리: 33.5 MB, 시간: 0.04 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

Empty

### 문제 설명

<p>정수 배열 <code>numbers</code>와 정수 <code>num1</code>, <code>num2</code>가 매개변수로 주어질 때, <code>numbers</code>의 <code>num1</code>번 째 인덱스부터 <code>num2</code>번째 인덱스까지 자른 정수 배열을 return 하도록 solution 함수를 완성해보세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>2 ≤ <code>numbers</code>의 길이 ≤ 30</li>
<li>0 ≤ <code>numbers</code>의 원소 ≤ 1,000</li>
<li>0 ≤<code>num1</code> &lt; <code>num2</code> &lt; <code>numbers</code>의 길이</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>numbers</th>
<th>num1</th>
<th>num2</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>[1, 2, 3, 4, 5]</td>
<td>1</td>
<td>3</td>
<td>[2, 3, 4]</td>
</tr>
<tr>
<td>[1, 3, 5]</td>
<td>1</td>
<td>2</td>
<td>[3, 5]</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>[1, 2, 3, 4, 5]의 1번째 인덱스 2부터 3번째 인덱스 4 까지 자른 [2, 3, 4]를 return 합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>[1, 3, 5]의 1번째 인덱스 3부터 2번째 인덱스 5까지 자른 [3, 5]를 return 합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges  <br><br>

<hr>

## 😀 나의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/07e51648-98ad-472f-8ae7-e2f9d36420a8) <br>
-> 반복문을 활용하여 num1, num2 까지 인덱스 값들로 접근해주었다. <br><br>

## ⭕ 다른 사람의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/85beb101-3cf6-4a5d-8a95-03f71c454772) <br>
-> js의 splice함수를 사용하여, 첫번째 매개변수부터 시작하여 두번째값의 갯수만큼 반복된다. <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/841201ac-b9f5-4704-9fa3-843f3bba1fed) <br>
-> slice함수를 사용하였다. 이 함수는 num1부터 시작하여, num2 인덱스 만큼 자르는 것이다. <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/e647211f-37ee-4631-aae3-fc1b296e9ceb) <br>
-> filter로 하는 풀이를 시도했었다. filter 함수의 두번째 매개변수는 인덱스를 의미한다. <br><br>

## ✔️ What I learned: <br>
- slice와 splice 함수: 두 개의 첫 번째 매개변수는 같지만, slice의 두번째 매개변수는 인덱스+1이고, splice의 두번째 인덱스는 갯수이다. <br>
