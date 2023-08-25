# [level 0] 특이한 정렬 - 120880 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120880?language=javascript) 

### 성능 요약

메모리: 33.4 MB, 시간: 0.07 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

Empty

### 문제 설명

<p>정수 <code>n</code>을 기준으로 <code>n</code>과 가까운 수부터 정렬하려고 합니다. 이때 <code>n</code>으로부터의 거리가 같다면 더 큰 수를 앞에 오도록 배치합니다. 정수가 담긴 배열 <code>numlist</code>와 정수 <code>n</code>이 주어질 때 <code>numlist</code>의 원소를 <code>n</code>으로부터 가까운 순서대로 정렬한 배열을 return하도록 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>n</code> ≤ 10,000</li>
<li>1 ≤ <code>numlist</code>의 원소 ≤ 10,000</li>
<li>1 ≤ <code>numlist</code>의 길이 ≤ 100</li>
<li><code>numlist</code>는 중복된 원소를 갖지 않습니다.</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>numlist</th>
<th>n</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>[1, 2, 3, 4, 5, 6]</td>
<td>4</td>
<td>[4, 5, 3, 6, 2, 1]</td>
</tr>
<tr>
<td>[10000,20,36,47,40,6,10,7000]</td>
<td>30</td>
<td>[36, 40, 20, 47, 10, 6, 7000, 10000]</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>4에서 가까운 순으로 [4, 5, 3, 6, 2, 1]을 return합니다.</li>
<li>3과 5는 거리가 같으므로 더 큰 5가 앞에 와야 합니다.</li>
<li>2와 6은 거리가 같으므로 더 큰 6이 앞에 와야 합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>30에서 가까운 순으로 [36, 40, 20, 47, 10, 6, 7000, 10000]을 return합니다.</li>
<li>20과 40은 거리가 같으므로 더 큰 40이 앞에 와야 합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges <br><br>

<hr>

## 😀 나의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/641a90e4-d244-43d1-bb18-5e2a0be00f88) <br>
-> 절댓값이 같으면 큰 수를 먼저 써줘야 하므로, numlist를 일단 정렬하였다. 그리고, n과 각 요소의 차이를 뺀 값을 담은 배열을 만든다. 그리고, 절댓값이 작은 것을 기준으로 그 배열 g를 정렬한다. 그리고, 그 순서에 따라 그 값에 해당하는 값을 answer에 push 시켜주는 것이다. 이건 오늘 앞서 풀었던, 하나의 배열 다른 배열의 기준에 따라 분류하는 문제유형이었다. <br><br>

## ⭕ 다른 사람의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/12b34492-50e0-4711-94aa-abdd30d12136) <br>
-> 절댓값을 기준으로 절댓값이 작은 것 부터 정렬하고, 0이 되면 (절댓값이 같으면) 더 큰 값을 먼저 정렬하라는 의미의 코드이다. <br><br>

## ✔️ What I learned: <br>  
- 하나의 배열을 어떤 또 다른 배열의 값을 기준으로 정렬하는 문제이다. 이런 문제는 기준 배열을 정렬한 또 다른 배열을 만들고, 그 배열의 인덱스로 접근하는 것!<br>
