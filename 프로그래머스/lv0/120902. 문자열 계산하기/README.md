# [level 0] 문자열 계산하기 - 120902 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120902) 

### 성능 요약

메모리: 33.4 MB, 시간: 0.05 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

Empty

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

## 🎁 나의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/49831107-f7b9-40b6-986b-2c49d7753367) <br>
-> 공백을 기준으로 식을 분리하였다. 연산자는 1번 인덱스부터 시작해서 1,3,5,,,이렇게 진행될 것이다. 따라서 arr배열의 길이만큼 반복하면서, 연산자에 접근하기 위해 i는 2를 더해주었고, 만약 '+'이면 그 다음 숫자를 더해주었고, 아니면 '-'이므로 빼주었다. 연산자는 +, -만 존재한다는 조건이 있어서, 삼항연산자로 쉽게 처리하였다. <br><br>

## ⭕ 다른 사람의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/ed0e438e-6f50-4927-8150-84de272e7cf0) <br>
-> 문자열로된 식의 값을 계산하는 함수이다. 하지만 사용하지 않는 게 좋을 것임!! <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/d441ee4e-37cb-4862-b3d1-a72a15e2a601) <br>
-> '+'이면 다음 숫자에 '+'을, '-'이면 다음 숫자에 '-'를 붙여 음수 처리를 해주었다. 그리고 숫자를 만나면 그 sign을 적용한 값을 push하고 마지막에 reduce를 통해 그 배열의 모든 값을 더해 반환하였다. 두번째 인자는 초기값을 의미한다!<br><br>

## ✔️ What I learned: <br> 
- parseInt는 floor 값이라는 것! <br>
- reduce 함수의 2번째 인자는 초깃값이다!!
