# [level 0] 7의 개수 - 120912 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120912?language=javascript) 

### 성능 요약

메모리: 33.4 MB, 시간: 0.07 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

Empty

### 문제 설명

<p>머쓱이는 행운의 숫자 7을 가장 좋아합니다. 정수 배열 <code>array</code>가 매개변수로 주어질 때, 7이 총 몇 개 있는지 return 하도록 solution 함수를 완성해보세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>array</code>의 길이 ≤ 100</li>
<li>0 ≤ <code>array</code>의 원소 ≤ 100,000</li>
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
<td>[7, 77, 17]</td>
<td>4</td>
</tr>
<tr>
<td>[10, 29]</td>
<td>0</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>[7, 77, 17]에는 7이 4개 있으므로 4를 return 합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>[10, 29]에는 7이 없으므로 0을 return 합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges <br><br>

<hr>

## 🎁 나의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/947b0a39-41fd-4452-bcc7-ec2182117f64) <br>
-> 배열 요소에 하나씩 접근하였다. 그리고 그 값을 문자열로 바꾸고, 그 문자열에서 '7'인 것만 필터링해서 그 갯수를 sum에 더해주었다. 그렇게 하면 array에 있는 모든 7의 갯수가 저장된다. <br><br>

## ⭕ 다른 사람의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/51a9801f-376a-4b00-9c6e-3b00a8e36ebc) <br>
-> <br>

## ✔️ What I learned: <br>  
