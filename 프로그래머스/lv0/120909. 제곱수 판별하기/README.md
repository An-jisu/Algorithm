# [level 0] 제곱수 판별하기 - 120909 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120909) 

### 성능 요약

메모리: 10.2 MB, 시간: 0.04 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

<br/>정확성: 100.0<br/>합계: 100.0 / 100.0

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


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges  <br><br>

<hr>

## 👑 나의 풀이: <br>
-> 주어진 수의 제곱근을 구하여, 그것이 1과 1000사이의 숫자이면, 1을 반환하게 하였따. 제곱근을 구한 후, 정수인지 판별하는 것에 대한 고민이 있었다.<br><br>

## ⭕ 다른 사람의 풀이: <br>
![image](https://user-images.githubusercontent.com/70849122/224597520-15bdbedf-bde2-4130-910b-fe88ad4646b9.png) <br>
-> 꼭 sqrt함수를 쓰지 않더라도, 0.5승을 하여 제곱근을 구할 수 있다는 것!! 또, int인지 확인하기 위한 is_integer() 함수가 있다는 것 <br><br>

## ✔ What I learned: <br>
- '**' 연산자: 거듭제곱 연산자!!!!
- 정수인지 판별하는 is_integer() 함수
- 제곱근 구하기: 0.5승, sqrt 함수 (math 라이브러리 임포트 해줘야 함)
