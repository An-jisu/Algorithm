# [level 1] 삼총사 - 131705 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/131705) 

### 성능 요약

메모리: 10 MB, 시간: 0.04 ms

### 구분

코딩테스트 연습 > 연습문제

### 채점결과

Empty

### 문제 설명

<p>한국중학교에 다니는 학생들은 각자 정수 번호를 갖고 있습니다. 이 학교 학생 3명의 정수 번호를 더했을 때 0이 되면 3명의 학생은 삼총사라고 합니다. 예를 들어, 5명의 학생이 있고, 각각의 정수 번호가 순서대로 -2, 3, 0, 2, -5일 때, 첫 번째, 세 번째, 네 번째 학생의 정수 번호를 더하면 0이므로 세 학생은 삼총사입니다. 또한, 두 번째, 네 번째, 다섯 번째 학생의 정수 번호를 더해도 0이므로 세 학생도 삼총사입니다. 따라서 이 경우 한국중학교에서는 두 가지 방법으로 삼총사를 만들 수 있습니다.</p>

<p>한국중학교 학생들의 번호를 나타내는 정수 배열 <code>number</code>가 매개변수로 주어질 때, 학생들 중 삼총사를 만들 수 있는 방법의 수를 return 하도록 solution 함수를 완성하세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>3 ≤ <code>number</code>의 길이 ≤ 13</li>
<li>-1,000 ≤ <code>number</code>의 각 원소 ≤ 1,000</li>
<li>서로 다른 학생의 정수 번호가 같을 수 있습니다.</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>number</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>[-2, 3, 0, 2, -5]</td>
<td>2</td>
</tr>
<tr>
<td>[-3, -2, -1, 0, 1, 2, 3]</td>
<td>5</td>
</tr>
<tr>
<td>[-1, 1, -1, 1]</td>
<td>0</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p><strong>입출력 예 #1</strong></p>

<ul>
<li>문제 예시와 같습니다.</li>
</ul>

<p><strong>입출력 예 #2</strong></p>

<ul>
<li>학생들의 정수 번호 쌍 (-3, 0, 3), (-2, 0, 2), (-1, 0, 1), (-2, -1, 3), (-3, 1, 2) 이 삼총사가 될 수 있으므로, 5를 return 합니다.</li>
</ul>

<p><strong>입출력 예 #3</strong></p>

<ul>
<li>삼총사가 될 수 있는 방법이 없습니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges  <br><br>

<hr>

## ❤️ 문제 핵심: <br>
-> 리스트에서 3개의 요소를 뽑아서 0이되는 경우의 수의 갯수를 구해야함. <br> 

## 😀 나의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/4623cd77-aea9-46c1-819d-2e5ecb67dc4d) <br>
-> 리스트에서 3개의 요소를 뽑는 것을 어떻게 처리할까에 대한 고민이 많아서, 오래걸렸던 문제...... 리스트를 하나 만들어서 돌아가면서 하나씩 push, pop해야하나.... 그렇게 복잡하게 푸는 게 아닐텐데...그래서 블로그에서 힌트를 얻었다. 삼중 반복문을 활용하여서 누군가가 풀었다는 것이다. 그래서 나도 그렇게 풀어보았고, 잘 실행되었다. 쉬운 문제였는데 내가 너무 복잡하게 생각했다는 것..<br><br>

## ⭕ 다른 사람의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/6af854f0-a9aa-4e69-ac65-4c101f90673c) <br>
-> itertools의 combinations이라는 라이브러리를 이용하였다. 그러면, 어느 리스트에서 몇 개를 뽑을 건지 인자로 넘겨주면, 리스트로 반환해준다. 그 리스트의 합이 0 인경우에만 cnt를 1 더해주었다. <br><br>

## ✔ What I learned: <br>
-> 리스트에서 특정 몇 개를 뽑는 것은 중첩 반복문을 활용할 수 있다는 것!! (몇 개 뽑는지 정해져있는 경우에 가능) <br>
-> 리스트에서 특정 요소 뽑기: from itertools import combinations/ combinations(리스트, 갯수) <br>
