# [level 0] 이진수 더하기 - 120885 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120885) 

### 성능 요약

메모리: 10.2 MB, 시간: 0.01 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

<br/>정확성: 100.0<br/>합계: 100.0 / 100.0

### 문제 설명

<p>이진수를 의미하는 두 개의 문자열 <code>bin1</code>과 <code>bin2</code>가 매개변수로 주어질 때, 두 이진수의 합을 return하도록 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>return 값은 이진수를 의미하는 문자열입니다.</li>
<li>1 ≤ <code>bin1</code>, <code>bin2</code>의 길이 ≤ 10</li>
<li><code>bin1</code>과 <code>bin2</code>는 0과 1로만 이루어져 있습니다.</li>
<li><code>bin1</code>과 <code>bin2</code>는 "0"을 제외하고 0으로 시작하지 않습니다.</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>bin1</th>
<th>bin2</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>"10"</td>
<td>"11"</td>
<td>"101"</td>
</tr>
<tr>
<td>"1001"</td>
<td>"1111"</td>
<td>"11000"</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>10 + 11 = 101 이므로 "101" 을 return합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>1001 + 1111 = 11000 이므로 "11000"을 return합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges  <br><br>

<hr>

## 👑 나의 풀이: <br>
-> 이 코드는 완전히 내가 짠 것은 아니고, 파이썬에 10진수를 2진수로 바꿔주는 함수가 있을 것이라고 생각되어 검색을 통해 참고하였다. 각각의 문자열을 int형 10진수로 바꿔준다. 그런데, 2번째 인수로 2를 주어 2진수라는 것을 나타낸다. 10진수로 바꾼 두 수를 더해서, bin함수를 통해 이진수로 바꿔준다. 그런데, 0b가 함께 출력되므로, 그것을 제거하기 위해 인덱싱으 활용한다. <br><br>

## ✔ What I learned: <br>
1. bin 함수: 10진수를 2진수로 바꿔주는 함수/변환하여 문자열 형태로 반환해준다. <br>
2. int 함수: 문자열을 10진수로 바꿔줄 때 많이 사용/ 두 번째 인수는 2진수임을 나타내는 것임을 기억하자!!!! <br>
3. 특정 문자를 제거하기 위해, 인덱싱을 활용하는 거 기억하기! <br><br>
