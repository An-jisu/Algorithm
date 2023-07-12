# [level 0] 분수의 덧셈 - 120808 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120808?language=javascript) 

### 성능 요약

메모리: 33.7 MB, 시간: 2.86 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

Empty

### 문제 설명

<p>첫 번째 분수의 분자와 분모를 뜻하는 <code>numer1</code>, <code>denom1</code>, 두 번째 분수의 분자와 분모를 뜻하는 <code>numer2</code>, <code>denom2</code>가 매개변수로 주어집니다. 두 분수를 더한 값을 기약 분수로 나타냈을 때 분자와 분모를 순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>0 &lt;<code>numer1</code>, <code>denom1</code>,&nbsp;<code>numer2</code>, <code>denom2</code> &lt; 1,000</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>numer1</th>
<th>denom1</th>
<th>numer2</th>
<th>denom2</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>1</td>
<td>2</td>
<td>3</td>
<td>4</td>
<td>[5, 4]</td>
</tr>
<tr>
<td>9</td>
<td>2</td>
<td>1</td>
<td>3</td>
<td>[29, 6]</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>1 / 2 + 3 / 4 = 5 / 4입니다. 따라서 [5, 4]를 return 합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>9 / 2 + 1 / 3 = 29 / 6입니다. 따라서 [29, 6]을 return 합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges  <br><br>

<hr>

## 🎁 나의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/759539ca-dcaa-479a-abfc-17e1350152c7) <br>
-> 분모를 곱한 값을 공통 분모로 하여, 그 각 값을 곱해 분자를 구한다. 그리고, 최대공약수로 분모와 분자를 나누어 배열에 담아 return 한다. 최대 공약수, 최소 공배수를 구하는것에 조금 어려움이 있었다. 최대 공약수, 최소 공배수 구하는 코드 외우자! <br><br>

## ⭕ 다른 사람의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/6df0e8cf-5220-44cb-bc7a-053d8b9d8faa) <br>
-> 최대공약수 함수를 만들어 처리하였다. 재귀함수를 이용해 최대공약수를 구했다. <br><br>


## ✔️ What I learned: <br>
<유클리드 호제법으로 최대 공약수 구하기><br>
a와 b의 나머지를 계산하여 나머지가 0이 될 때까지 계속해서 적용하고, 최종적으로 0인 나머지의 앞의 값이 최대공약수! <br>
<유클리드 호제법으로 최소 공배수 구하기><br>
-> 유클리드 호제법으로 구한 최대 공약수로 두 수의 곱을 나누어주면 된다!! <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/32483f8b-e969-456f-9091-302ca71cf525) <br>
-> 둘 다 외우기!!!
