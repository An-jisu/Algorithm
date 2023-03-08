# [level 0] 대문자와 소문자 - 120893 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120893) 

### 성능 요약

메모리: 10.1 MB, 시간: 0.31 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

<br/>정확성: 100.0<br/>합계: 100.0 / 100.0

### 문제 설명

<p>문자열 <code>my_string</code>이 매개변수로 주어질 때, 대문자는 소문자로 소문자는 대문자로 변환한 문자열을 return하도록 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>my_string</code>의 길이 ≤ 1,000</li>
<li><code>my_string</code>은 영어 대문자와 소문자로만 구성되어 있습니다.</li>
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
<td>"cccCCC"</td>
<td>"CCCccc"</td>
</tr>
<tr>
<td>"abCdEfghIJ"</td>
<td>"ABcDeFGHij"</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>소문자는 대문자로 대문자는 소문자로 바꾼 "CCCccc"를 return합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>소문자는 대문자로 대문자는 소문자로 바꾼 "ABcDeFGHij"를 return합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges  <br><br>

<hr>

## 👑 나의 풀이: <br>
: 내장함수들을 이용하여, 대소문자를 바꿔주었음 <br><br>

## ⭕ 다른 사람의 풀이: <br>
![image](https://user-images.githubusercontent.com/70849122/223640953-5eeddc2b-bcb7-410d-a747-94f45f53242a.png) <br>
-> swapcase라는 함수를 통해 대소문자를 서로 바꿀 수 있음!!<br><br>

## ✔ What I learned: <br>
- i.isupper()/ i.islower()
- i.upper()/ i.lower()
-> 대소문자 바꿔서 반환해주는 함수 잘 기억하기!! 기존꺼를 바꿔주는 것이 아닌 바꿔서 
