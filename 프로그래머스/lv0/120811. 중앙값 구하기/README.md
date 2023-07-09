# [level 0] 중앙값 구하기 - 120811 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120811?language=javascript) 

### 성능 요약

메모리: 33.5 MB, 시간: 0.04 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

Empty

### 문제 설명

<p>중앙값은 어떤 주어진 값들을 크기의 순서대로 정렬했을 때 가장 중앙에 위치하는 값을 의미합니다. 예를 들어 1, 2, 7, 10, 11의 중앙값은 7입니다. 정수 배열 <code>array</code>가 매개변수로 주어질 때, 중앙값을 return 하도록 solution 함수를 완성해보세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li><code>array</code>의 길이는 홀수입니다.</li>
<li>0 &lt; <code>array</code>의 길이 &lt; 100</li>
<li>-1,000 &lt; <code>array</code>의 원소 &lt; 1,000</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>array</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>[1, 2, 7, 10, 11]</td>
<td>7</td>
</tr>
<tr>
<td>[9, -1, 0]</td>
<td>0</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>본문과 동일합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>9, -1, 0을 오름차순 정렬하면 -1, 0, 9이고 가장 중앙에 위치하는 값은 0입니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges  <br><br>

<hr>

## 🎁 나의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/8d2a6a23-21c5-43eb-9cc0-a3b3da48fb82) <br>
-> sort 함수를 통해 오름차순으로 정렬(a-b)하고, math.floor을 이용하여 가운뎃 값을 반환하였다. <br><br>

## ⭕ 다른 사람의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/62a23b59-261c-4f2a-a9e0-0e6fd686f5ba) <br>
-> 내가 푼 방법과 유사하지만, sort이후 .at함수를 또 사용하였다. at함수는 정수를 받아 그 정수 인덱스에 해당하는 요소를 반환한다. 이게 더 가독성 좋은 풀이다!! <br>

## ✔️ What I learned: <br>
- at 함수: 정수를 받아 그 정수 인덱스 값에 해당하는 요소의 값을 반환한다. <br>
- js에도 sort함수를 통해 정렬할 수 있다는 것!!(여기서는 화살표 함수로 오름차순이면, a-b 이렇게 나타내야 한다.)
