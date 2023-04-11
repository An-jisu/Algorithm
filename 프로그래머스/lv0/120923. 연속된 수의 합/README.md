# [level 0] 연속된 수의 합 - 120923 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120923) 

### 성능 요약

메모리: 10.2 MB, 시간: 0.01 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

<br/>정확성: 100.0<br/>합계: 100.0 / 100.0

### 문제 설명

<p>연속된 세 개의 정수를 더해 12가 되는 경우는 3, 4, 5입니다. 두 정수 <code>num</code>과 <code>total</code>이 주어집니다. 연속된 수 <code>num</code>개를 더한 값이 <code>total</code>이 될 때, 정수 배열을 오름차순으로 담아 return하도록 solution함수를 완성해보세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>num</code> ≤ 100</li>
<li>0 ≤ <code>total</code> ≤ 1000</li>
<li><code>num</code>개의 연속된 수를 더하여 <code>total</code>이 될 수 없는 테스트 케이스는 없습니다.</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>num</th>
<th>total</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>3</td>
<td>12</td>
<td>[3, 4, 5]</td>
</tr>
<tr>
<td>5</td>
<td>15</td>
<td>[1, 2, 3, 4, 5]</td>
</tr>
<tr>
<td>4</td>
<td>14</td>
<td>[2, 3, 4, 5]</td>
</tr>
<tr>
<td>5</td>
<td>5</td>
<td>[-1, 0, 1, 2, 3]</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li><code>num</code> = 3, <code>total</code> = 12인 경우 [3, 4, 5]를 return합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li><code>num</code> = 5, <code>total</code> = 15인 경우 [1, 2, 3, 4, 5]를 return합니다.</li>
</ul>

<p>입출력 예 #3</p>

<ul>
<li>4개의 연속된 수를 더해 14가 되는 경우는 2, 3, 4, 5입니다.</li>
</ul>

<p>입출력 예 #4</p>

<ul>
<li>설명 생략</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges  <br><br>

<hr>

## 👑 나의 풀이: <br>
![image](https://user-images.githubusercontent.com/70849122/231048008-448acb9a-4dd7-4b55-aea1-38fa1a5e04cb.png) <br>
-> 처음에는 이렇게 코딩을 했는데, 3개의 테스트케이스에서 오류가 나는 것이다.<br><br>

## ⭕ 다른 사람의 풀이: <br>
![image](https://user-images.githubusercontent.com/70849122/231048784-32b0fded-a9f3-4d82-a880-1ca3710385b0.png) <br>
![image](https://user-images.githubusercontent.com/70849122/231048829-4fc45236-3193-4ec3-97c5-74e08aac7e91.png) <br>
![image](https://user-images.githubusercontent.com/70849122/231048978-965598f9-a1e8-4c83-ae29-a313730d3eef.png)<br>
-> 등차수열의 첫째항은, num까지의 합을 구하고 total에서 빼서 num으로 나눈 값으로 구할 수 있다는 것!!<br><br>

## 다시 풀어보기!!!
