# [level 0] 배열의 평균값 - 120817 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120817?language=javascript) 

### 성능 요약

메모리: 33.4 MB, 시간: 0.03 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

Empty

### 문제 설명

<p>정수 배열 <code>numbers</code>가 매개변수로 주어집니다. <code>numbers</code>의 원소의 평균값을 return하도록 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>0 ≤ <code>numbers</code>의 원소 ≤ 1,000</li>
<li>1 ≤ <code>numbers</code>의 길이 ≤ 100</li>
<li>정답의 소수 부분이 .0 또는 .5인 경우만 입력으로 주어집니다. </li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>numbers</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]</td>
<td>5.5</td>
</tr>
<tr>
<td>[89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]</td>
<td>94.0</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li><code>numbers</code>의 원소들의 평균 값은 5.5입니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li><code>numbers</code>의 원소들의 평균 값은 94.0입니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges <br><br>

<hr>

## 🎁 나의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/de4bc013-ea0b-4433-b54d-69a456f27100) <br>
-> js에서는 for문을 잘 사용하지 않아, map함수로 처리하려고 하였으나 그 사용법을 아직 잘 익히지 않아 for문으로 처리하였다. <br><br>

## ⭕ 다른 사람의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/3355da46-0bd5-46b1-b79d-dcf565f0e429) <br>
-> reduce함수를 통해서 합을 구하고 배열의 길이로 나누어 평균을 구하였다. <br><br>

## ✔️ What I learned: <br>
- reduce: 배열의 각 요소 순회하며, 함수 실행 값 누적하여 하나의 결괏값 반환 <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/d30f4f3d-91d1-4f9e-a448-4b0e78daa80f) <br>
-> 즉, 첫 매개변수에 계속해서 값이 누적되는 것임!!
