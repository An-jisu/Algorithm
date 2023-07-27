# [level 0] 인덱스 바꾸기 - 120895 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120895?language=javascript) 

### 성능 요약

메모리: 33.4 MB, 시간: 0.04 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

Empty

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

## 🎁 나의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/8066d3ea-e543-43ea-ba02-8207f680c519) <br>
-> 문자열은 변경할 수 없기 때문에, 배열로 변환하여 각 요소들을 temp변수를 이용하여 변환 후, 문자열로 join 한다. <br><br>

## ⭕ 다른 사람의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/f726bdfd-5377-4020-bf09-0eee5833226e) <br>
-> 값의 변경을 temp 변수를 이용하지 않고, 위와 같이 스위치를 할 수 있다. 구조분해 할당!!!!!!<br><br>

## ✔️ What I learned: <br>
- 배열에서 2개의 값 교환: 구조 분해 할당으로!!! <br>
