# [level 0] 최댓값 만들기 (1) - 120847 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120847) 

### 성능 요약

메모리: 10.1 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

<br/>정확성: 100.0<br/>합계: 100.0 / 100.0

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


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges <hr>

<br><br>

## 👑 나의 풀이: <br>
-> 최댓값을 구하고, 그 값을 배열에서 없앤 후, 다음 최댓값을 구한다. 그리고 곱한다.

## ⭕ 다른 사람의 풀이: <br>
![image](https://user-images.githubusercontent.com/70849122/222963447-ce8e5107-a1ad-402b-b41a-0cf3bcb53e6a.png) <br>
-> 정렬을 해서, 마지막 2개의 요소들을 곱한다. <br>
![image](https://user-images.githubusercontent.com/70849122/222963547-303d794c-4722-491b-aecb-8849756a2bfe.png) <br>
-> 뒤집어 정렬을 해서, 처음 2개의 요소들을 곱한다. <br>
