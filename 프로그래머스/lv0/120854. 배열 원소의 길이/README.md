# [level 0] 배열 원소의 길이 - 120854 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120854?language=javascript) 

### 성능 요약

메모리: 33.4 MB, 시간: 0.03 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

Empty

### 문제 설명

<p>문자열 배열 <code>strlist</code>가 매개변수로 주어집니다. <code>strlist</code> 각 원소의 길이를 담은 배열을 retrun하도록 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>strlist</code> 원소의 길이 ≤ 100</li>
<li><code>strlist</code>는 알파벳 소문자, 대문자, 특수문자로 구성되어 있습니다.</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>strlist</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>["We", "are", "the", "world!"]</td>
<td>[2, 3, 3, 6]</td>
</tr>
<tr>
<td>["I", "Love", "Programmers."]</td>
<td>[1, 4, 12]</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>["We", "are", "the", "world!"]의 각 원소의 길이인 [2, 3, 3, 6]을 return합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>["I", "Love", "Programmers."]의 각 원소의 길이인 [1, 4, 12]을 return합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges <br><br>

<hr>

## 🎁 나의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/20ac067a-8cbc-48dd-bb65-b0b009911d6b) <br>
-> map 함수를 통해 str_list 요소들의 길이를 각각 반복해서 구해주었다. 결괏값은 배열이다. <br><br>

## ⭕ 다른 사람의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/d2d521e5-b1f2-43d1-879a-123c469d4f3d) <br>
-> a는 배열의 누적값이고, b의 길이 값을 계속 추가해간다. <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/a089054d-9d6a-456d-a44a-490a3d30bd3e) <br>
-> 나와 같은 풀이이지만, forEach문을 활용하였다. <br>
