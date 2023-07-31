# [level 0] 제곱수 판별하기 - 120909 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120909?language=javascript) 

### 성능 요약

메모리: 33.4 MB, 시간: 0.04 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

Empty

### 문제 설명

<p>어떤 자연수를 제곱했을 때 나오는 정수를 제곱수라고 합니다. 정수 <code>n</code>이 매개변수로 주어질 때, <code>n</code>이 제곱수라면 1을 아니라면 2를 return하도록 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>n</code> ≤ 1,000,000</li>
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
<td>144</td>
<td>1</td>
</tr>
<tr>
<td>976</td>
<td>2</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>144는 12의 제곱이므로 제곱수입니다. 따라서 1을 return합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>976은 제곱수가 아닙니다. 따라서 2를 return합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges <br><br>

<hr>

## ⭕ 다른 사람의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/b5f30c75-3d1a-4f08-a780-9ea143950f08) <br>
-> sqrt통해 제곱근값 구한 그 긊이 정수인지 판별! <br>

## ✔️ What I learned: <br>
-> sqrt나 **연산 결과는 소수점까지 나온다!<br>
- 제곱근 판별 알고리즘: 루트 값 구한 것이(sqrt, **)이 정수인지 판별하기<br>
