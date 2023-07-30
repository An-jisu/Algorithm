# [level 0] 자릿수 더하기 - 120906 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120906?language=javascript) 

### 성능 요약

메모리: 33.3 MB, 시간: 0.04 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

Empty

### 문제 설명

<p>정수 <code>n</code>이 매개변수로 주어질 때 <code>n</code>의 각 자리 숫자의 합을 return하도록 solution 함수를 완성해주세요</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>0 ≤ <code>n</code> ≤ 1,000,000</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>n</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>1234</td>
<td>10</td>
</tr>
<tr>
<td>930211</td>
<td>16</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>1 + 2 + 3 + 4 = 10을 return합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>9 + 3 + 0 + 2 + 1 + 1 = 16을 return합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges  <br><br>

<hr>

## 🎁 나의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/990ec3e0-6c7a-43aa-bc12-b05ed684d73b) <br>
-> reduce의 2번째 매개변수를 처음에 써주지 않았더니, 초깃값을 문자열로 생각하여 처리되어 제대로 결괏값이 나오지 않았다. 따라서 숫자 문자열 배열의 모든 요소의 합을 구하기 위해서는 reduce 두번째 매개변수를 통해 초깃값을 지정해줘야 한다!! <br><br>

## ⭕ 다른 사람의 풀이: <br>

## ✔️ What I learned: <br> 
- 정수를 문자열로 표현할 때, toString으로 할 수 있다는 것! 2가지가 다 골고루 연습하자!
