# [level 0] 문자열 계산하기 - 120902 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120902) 

### 성능 요약

메모리: 10.3 MB, 시간: 0.02 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

<br/>정확성: 100.0<br/>합계: 100.0 / 100.0

### 문제 설명

<p><code>my_string</code>은 "3 + 5"처럼 문자열로 된 수식입니다. 문자열 <code>my_string</code>이 매개변수로 주어질 때, 수식을 계산한 값을 return 하는 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>연산자는 +, -만 존재합니다.</li>
<li>문자열의 시작과 끝에는 공백이 없습니다.</li>
<li>0으로 시작하는 숫자는 주어지지 않습니다.</li>
<li>잘못된 수식은 주어지지 않습니다.</li>
<li>5 ≤ <code>my_string</code>의 길이 ≤ 100</li>
<li><code>my_string</code>을&nbsp;계산한 결과값은 1 이상 100,000 이하입니다.

<ul>
<li><code>my_string</code>의 중간 계산 값은 -100,000 이상 100,000 이하입니다.</li>
<li>계산에 사용하는 숫자는 1 이상 20,000 이하인 자연수입니다.</li>
<li><code>my_string</code>에는 연산자가 적어도 하나 포함되어 있습니다.</li>
</ul></li>
<li>return type 은 정수형입니다.</li>
<li><code>my_string</code>의 숫자와 연산자는 공백 하나로 구분되어 있습니다.</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>my_string</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>"3 + 4"</td>
<td>7</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>3 + 4 = 7을 return 합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges <br><br>

<hr>

## 👑 나의 풀이: <br>
-> 일단 result 변수에 첫번째 숫자가 저장되어 있다고 가정하고, 반복문을 통해 연산자 부분에만 접근하도록 하였다. 조건문을 이용해서, +이거나 -일 때 그 다음 값을 result 결과에 처리하도록 하였다. <br><br>

## ⭕ 다른 사람의 풀이: <br>
![image](https://user-images.githubusercontent.com/70849122/224476371-758db233-4b56-4fd2-9f51-c1700136a959.png) <br>
-> '-'를 음수를 더하는 형태로 바꿔주고, 공백을 기준으로 분리하였다. 그 후 모든 요소들을 int로 바꿔서, 합을 구해주었다. <br>
![image](https://user-images.githubusercontent.com/70849122/224476390-6dadb3b0-f021-443b-bcb9-07039979f5ad.png) <br>
-> eval 함수 이용<br><br>

## ✔ What I learned: <br><br>
-> eval 함수는 매개변수를 식을 문자열로 받아서 계산을 수행하는 함수이다. int 형으로 바꿔서 반환해준다. 
