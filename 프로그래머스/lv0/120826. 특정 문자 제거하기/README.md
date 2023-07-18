# [level 0] 특정 문자 제거하기 - 120826 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120826?language=javascript) 

### 성능 요약

메모리: 33.4 MB, 시간: 0.05 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

Empty

### 문제 설명

<p>문자열 <code>my_string</code>과 문자 <code>letter</code>이 매개변수로 주어집니다. <code>my_string</code>에서 <code>letter</code>를 제거한 문자열을 return하도록 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>my_string</code>의 길이 ≤ 100</li>
<li><code>letter</code>은 길이가 1인 영문자입니다.</li>
<li><code>my_string</code>과 <code>letter</code>은 알파벳 대소문자로 이루어져 있습니다.</li>
<li>대문자와 소문자를 구분합니다.</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>my_string</th>
<th>letter</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>"abcdef"</td>
<td>"f"</td>
<td>"abcde"</td>
</tr>
<tr>
<td>"BCBdbe"</td>
<td>"B"</td>
<td>"Cdbe"</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>"abcdef" 에서 "f"를 제거한 "abcde"를 return합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>"BCBdbe" 에서 "B"를 모두 제거한 "Cdbe"를 return합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges <br><br>

<hr>

## 😀 나의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/3ac3797b-4491-4e6e-a76f-f40282d7e6af) <br>
-> string을 [...my_string]을 통해 배열로 바꾸고, filter함수를 통해 letter와 다른 것만 남겼다. 그리고 join으로 문자열로 다시 묶어주었다. <br><br>

## ⭕ 다른 사람의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/18571dea-6f97-4494-806a-84b98e5825db) <br>
-> letter라는 문자를 기준으로 분리한다. split이 파이썬과 달리, 특정 문자를 기준으로 분리하여 제거하여 배열로 만들어준다<br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/22b02e33-557d-4df9-a9bd-9f5da8ca8d8c) <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/0d7491de-db67-4996-b83e-67894b6900f3) <br>
-> replaceAll 함수를 이용해서 letter를 모두 ""로 대체하였다. <br><br>

## ✔️ What I learned: <br>
-> filter함수의 조건문에서는 제거할 것이 아닌 남겨둘 것의 조건을 적어준다. <br>
> js에는 replaceAll이 있다. 특정 문자를 교체하는 것!!! 파이썬의 replace함수임. <br>
-> js의 split함수는 파이썬의 split함수와 달리, 특정 문자를 기준으로 분리하여 제거한다!! 파이썬에서는 단지 분리!!!! <br><br>
