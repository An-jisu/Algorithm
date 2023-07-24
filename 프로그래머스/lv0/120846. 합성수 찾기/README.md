# [level 0] 합성수 찾기 - 120846 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120846?language=javascript) 

### 성능 요약

메모리: 33.3 MB, 시간: 0.11 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

Empty

### 문제 설명

<p>약수의 개수가 세 개 이상인 수를 합성수라고 합니다. 자연수 <code>n</code>이 매개변수로 주어질 때 <code>n</code>이하의 합성수의 개수를 return하도록 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>n</code> ≤ 100</li>
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
<td>10</td>
<td>5</td>
</tr>
<tr>
<td>15</td>
<td>8</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>10 이하 합성수는 4, 6, 8, 9, 10 로 5개입니다. 따라서 5를 return합니다.</li>
</ul>

<p>입출력 예 #1</p>

<ul>
<li>15 이하 합성수는 4, 6, 8, 9, 10, 12, 14, 15 로 8개입니다. 따라서 8을 return합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges  <br><br>

<hr>

## 🎁 나의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/06b34698-2b8e-45b7-bb0a-b9de20e844f7) <br>
-> n까지 하나씩 접근하면서, 각각이 합성수인지 검사한다. 각각이 합성수 인지는 i까지 모두 검사하는 것이 아니라, 제곱근값까지의 약수의 갯수를 구한다. 2부터 시작하게끔 하여, 만약 나누어떨어지는 수가 하나라도 있다면 합성수로 처리해서 answer의 값을 1 증가시켰다.  <br><br>
