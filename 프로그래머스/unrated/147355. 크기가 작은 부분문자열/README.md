# [unrated] 크기가 작은 부분문자열 - 147355 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/147355) 

### 성능 요약

메모리: 10.3 MB, 시간: 0.03 ms

### 구분

코딩테스트 연습 > 연습문제

### 채점결과

Empty

### 문제 설명

<p>숫자로 이루어진 문자열 <code>t</code>와 <code>p</code>가 주어질 때, <code>t</code>에서 <code>p</code>와 길이가 같은 부분문자열 중에서, 이 부분문자열이 나타내는 수가 <code>p</code>가 나타내는 수보다 작거나 같은 것이 나오는 횟수를 return하는 함수 solution을 완성하세요.</p>

<p>예를 들어, <code>t</code>="3141592"이고 <code>p</code>="271" 인 경우, <code>t</code>의 길이가 3인 부분 문자열은 314, 141, 415, 159, 592입니다. 이 문자열이 나타내는 수 중 271보다 작거나 같은 수는 141, 159 2개 입니다.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>p</code>의 길이 ≤ 18</li>
<li><code>p</code>의 길이 ≤ <code>t</code>의 길이 ≤ 10,000</li>
<li><code>t</code>와 <code>p</code>는 숫자로만 이루어진 문자열이며, 0으로 시작하지 않습니다.</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>t</th>
<th>p</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>"3141592"</td>
<td>"271"</td>
<td>2</td>
</tr>
<tr>
<td>"500220839878"</td>
<td>"7"</td>
<td>8</td>
</tr>
<tr>
<td>"10203"</td>
<td>"15"</td>
<td>3</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1<br>
본문과 같습니다.</p>

<p>입출력 예 #2<br>
<code>p</code>의 길이가 1이므로 <code>t</code>의 부분문자열은 "5", "0", 0", "2", "2", "0", "8", "3", "9", "8", "7", "8"이며 이중 7보다 작거나 같은 숫자는 "5", "0", "0", "2", "2", "0", "3", "7" 이렇게 8개가 있습니다.</p>

<p>입출력 예 #3<br>
<code>p</code>의 길이가 2이므로 <code>t</code>의 부분문자열은 "10", "02", "20", "03"이며, 이중 15보다 작거나 같은 숫자는 "10", "02", "03" 이렇게 3개입니다. "02"와 "03"은 각각 2, 3에 해당한다는 점에 주의하세요</p>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges  <br><br>

<hr>
## ❤️ 문제 핵심: <br>
-> p의 길이만큼, t에서 나올 수 있는 값들 중에서 p의 값보다 작거나 같은 값의 개수를 반환하는 문제이다. <br><br>

## 😀 나의 풀이: <br>
-> 이번 문제는 비교적 쉽게 빠르게 풀었다. <br>
![image](https://user-images.githubusercontent.com/70849122/236428642-b8de5b98-0d7d-4bac-b7c6-cf3e69945c8e.png) <br>
-> 일단, p의 자리수와 int값을 저장해두었다. 그리고 반복문을 돌면서, t에서 첫번째 값부터 접근하면서 p의 자리수만큼 t에서의 값을 얻었다. 그 t에서 값을 얻는 과정에서 약간의 고민이 되었는데, 리스트의 인덱싱 방법을 이용하였다. i부터 3개를 가져오면 되므로, [i:i+p의길이]이므로 i+p-1의 인덱스까지 가져올 것이다. 그 값을 int로 바꿔서 그게 p의 값보다 작거나 같으면, answer값을 증가시켰고, 최종적으로는 그 answer을 반환하였다. <br><br>

## ⭕ 다른 사람의 풀이: <br>
![image](https://user-images.githubusercontent.com/70849122/236429783-1e01dfc5-18a3-4b3e-b862-6b2a1a009ed6.png) <br>
-> 여기서는 인덱싱을 이렇게 간단하게 접근하였다!!<br><br>

## ✔️ What I learend: <br>
- 리스트나 문자열에서 특정 인덱스부터 특정갯수만큼의 값을 가져올 때, [:]이렇게 인덱싱 방법을 이용하자!
