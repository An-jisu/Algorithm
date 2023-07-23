# [level 0] 최댓값 만들기 (1) - 120847 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120847?language=javascript) 

### 성능 요약

메모리: 33.6 MB, 시간: 4.12 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

Empty

### 문제 설명

<p>정수 배열 <code>numbers</code>가 매개변수로 주어집니다. <code>numbers</code>의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return하도록 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>0 ≤ <code>numbers</code>의 원소 ≤ 10,000</li>
<li>2 ≤ <code>numbers</code>의 길이 ≤ 100</li>
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
<td>[1, 2, 3, 4, 5]</td>
<td>20</td>
</tr>
<tr>
<td>[0, 31, 24, 10, 1, 9]</td>
<td>744</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>두 수의 곱중 최댓값은 4 * 5 = 20 입니다.</li>
</ul>

<p>입출력 예 #1</p>

<ul>
<li>두 수의 곱중 최댓값은 31 * 24 = 744 입니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges <br><br>

<hr>

## 🎁 나의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/cd3663c6-18af-48c6-bb2e-5fa6c9c45fad) <br>
-> 오름차순해서, 끝의 두 값을 곱해서 반환해주었다. <br><br>

## ⭕ 다른 사람의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/7aa151f6-188e-4961-99b5-3b0b5dfa29d1) <br>
-> 여기서는 내림차순해서, 처음 두 수의 값을 곱해서 반환하였다. 오름차순만 생각했는데, 반대로하 조금 더 간결해졌다. <br>
-> at은 지정한 인덱스의 요소에 접근할 때 사용하는 메서드이다.<br><br>

## ✔️ What I learned: <br> 
- js오름차순(a-b), 내림차순(b-a) 코드 외우기!!
<br><br>
