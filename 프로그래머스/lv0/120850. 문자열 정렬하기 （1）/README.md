# [level 0] 문자열 정렬하기 (1) - 120850 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120850?language=javascript) 

### 성능 요약

메모리: 33.5 MB, 시간: 0.14 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

Empty

### 문제 설명

<p>문자열 <code>my_string</code>이 매개변수로 주어질 때, <code>my_string</code> 안에 있는 숫자만 골라 오름차순 정렬한 리스트를&nbsp;return 하도록 solution 함수를 작성해보세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>my_string</code>의 길이 ≤ 100</li>
<li><code>my_string</code>에는 숫자가 한 개 이상 포함되어 있습니다.</li>
<li><code>my_string</code>은 영어 소문자 또는 0부터 9까지의 숫자로 이루어져 있습니다.
- - -</li>
</ul>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>my_string</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>"hi12392"</td>
<td>[1, 2, 2, 3, 9]</td>
</tr>
<tr>
<td>"p2o4i8gj2"</td>
<td>[2, 2, 4, 8]</td>
</tr>
<tr>
<td>"abcde0"</td>
<td>[0]</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>"hi12392"에 있는 숫자 1, 2, 3, 9, 2를 오름차순 정렬한 [1, 2, 2, 3, 9]를 return 합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>"p2o4i8gj2"에 있는 숫자 2, 4, 8, 2를 오름차순 정렬한 [2, 2, 4, 8]을 return 합니다.</li>
</ul>

<p>입출력 예 #3</p>

<ul>
<li>"abcde0"에 있는 숫자 0을 오름차순 정렬한 [0]을 return 합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges <br><br>

<hr>

## 🎁 나의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/a15616bc-c392-4be7-824c-7a95e7b3a978) <br>
-> my_string을 각 요소를 배열에 분리하여 담는다. 그리고, number로 바꾼 것이 int형인 것만 남기도록 하였다. 그리고 각 요소를 문자열에서 int로 바꿔야하므로 map함수를 통해 처리하였고, 마지막으로 오름차순으로(a-b)정렬 후 반환하였다. <br><br>

## ⭕ 다른 사람의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/3ca2ff1b-2f42-4cf0-8d8d-e6e1f019d6d5) <br>
-> 인자에 포함된 문자를 찾으면, 이를 반환한다. 따라서 정규식에 포함된 문자를 찾아 숫자만 분리하고, 오름차순으로 정렬한다. 그리고 map함수를 이용해 Number로 바꿔주었다. <br><br>

## ✔️ What I learned: <br> 
- Number: 문자를 정수로 바꿔줌 <br>
- Number.isInteger(), Number.isNan() <br>
