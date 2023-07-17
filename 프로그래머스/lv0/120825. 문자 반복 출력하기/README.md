# [level 0] 문자 반복 출력하기 - 120825 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120825?language=javascript) 

### 성능 요약

메모리: 33.4 MB, 시간: 0.04 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

Empty

### 문제 설명

<p>문자열 <code>my_string</code>과 정수 <code>n</code>이 매개변수로 주어질 때, <code>my_string</code>에 들어있는 각 문자를 <code>n</code>만큼 반복한 문자열을 return 하도록 solution 함수를 완성해보세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>2 ≤ <code>my_string</code> 길이 ≤ 5</li>
<li>2 ≤ <code>n</code> ≤ 10</li>
<li>"my_string"은 영어 대소문자로 이루어져 있습니다.</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>my_string</th>
<th>n</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>"hello"</td>
<td>3</td>
<td>"hhheeellllllooo"</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>"hello"의 각 문자를 세 번씩 반복한 "hhheeellllllooo"를 return 합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges <br><br>

<hr>

## 😀 나의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/dd8fe170-2b17-4a79-be6c-d3a47d22f32b) <br>
-> 중첩 반복문을 활용해 처리하였다. my_string의 길이만큼 반복하면서 각 글자에 대해서는 n만큼 씩 반복한다. <br><br>

## ⭕ 다른 사람의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/a4040920-1db8-4134-9ce1-f45aa021639d) <br>
-> my_string.split("")을 [...my_string] 이라고 나타내었다. 각 문자를 분리하고, 각 문자를 n번씩 map함수를 통해 반복하였다. 이런 것을 구조분해 할당이라고 한다.<br> 
![image](https://github.com/An-jisu/Algorithm/assets/70849122/b11af9ac-d20c-48b2-bb8c-b4762bc25386) <br>
-> <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/5b19cc00-9da4-4501-8e5b-f8186bb322aa) <br>
-> <br><br>

## ✔ What I learned: <br>
- 각 요소에 대해서 같은 동작을 적용시키기 위해서는 map함수를 사용한다. <br>
- <br>
