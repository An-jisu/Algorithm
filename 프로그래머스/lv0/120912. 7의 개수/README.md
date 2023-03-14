# [level 0] 7의 개수 - 120912 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120912) 

### 성능 요약

메모리: 10.1 MB, 시간: 0.01 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

<br/>정확성: 100.0<br/>합계: 100.0 / 100.0

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


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges  <br><br>


<hr>

## 👑 나의 풀이: <br>
-> 반복문을 돌면서, 배열의 요소 하나하나에 접근해서, 그 정수를 string으로 바꾼 다음, 그 문자열 안에서 '7'의 개수를 더해서 answer변수에 더해주어 최종적으로 반환하였다. <br><br>

## ⭕ 다른 사람의 풀이: <br>
![image](https://user-images.githubusercontent.com/70849122/224945635-3372206e-6b05-438f-98c7-f5958c99effd.png) <br>
-> 헐....^^ 7의 총 개수이므로 굳이, 각 정수를 생각할 필요가 없었다..... 총 7의 개수를 세어주었으면 된다. 
