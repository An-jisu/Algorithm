# [level 0] 인덱스 바꾸기 - 120895 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120895) 

### 성능 요약

메모리: 10.3 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

<br/>정확성: 100.0<br/>합계: 100.0 / 100.0

### 문제 설명

<p>문자열 <code>my_string</code>과 정수 <code>num1</code>, <code>num2</code>가 매개변수로 주어질 때, <code>my_string</code>에서 인덱스 <code>num1</code>과 인덱스 <code>num2</code>에 해당하는 문자를 바꾼 문자열을 return 하도록 solution 함수를 완성해보세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 &lt; <code>my_string</code>의 길이 &lt; 100</li>
<li>0 ≤ <code>num1</code>, <code>num2</code> &lt; <code>my_string</code>의 길이</li>
<li><code>my_string</code>은 소문자로 이루어져 있습니다.</li>
<li><code>num1</code> ≠ <code>num2</code></li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>my_string</th>
<th>num1</th>
<th>num2</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>"hello"</td>
<td>1</td>
<td>2</td>
<td>"hlelo"</td>
</tr>
<tr>
<td>"I love you"</td>
<td>3</td>
<td>6</td>
<td>"I l veoyou"</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>"hello"의 1번째 인덱스인 "e"와 2번째 인덱스인 "l"을 바꾸면 "hlelo"입니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>"I love you"의 3번째 인덱스 "o"와 " "(공백)을 바꾸면 "I l veoyou"입니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges <br><br>


<hr>

## 👑 나의 풀이: <br>
-> 처음에는 문자열의 인덱스에 직접 접근해서 변경하는 방법을 사용하였다. 그런데, str이 callable 하지 않다는 오류가 뜨고.......... 그래서 num1, num2 인덱스가 나오면, 그때 값을 변경하는 것으로 코드를 수정했는데 역시나 코드가 돌아가지 않았다..... 그래서 인터넷을 참고하여 푼 문제!!!!

## ✔ What I learned: <br>
-> 문자열은 상숫값이므로, 인덱스에 직접 접근해서 값을 변경하는 것이 불가하다는 것 !!!!!!!!! 꼭, 기억하기!!!!! 문자열 인덱싱 불가!!!!
c언어에서도 마찬가지이다. 파이썬은, 웬만한 건 다 되는 언어라고 생각해서, 이 또한 될 것이라고 생각했다..ㅎㅎ
