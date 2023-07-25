# [level 0] 컨트롤 제트 - 120853 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120853?language=javascript) 

### 성능 요약

메모리: 33.4 MB, 시간: 0.14 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

Empty

### 문제 설명

<p>숫자와 "Z"가 공백으로 구분되어 담긴 문자열이 주어집니다. 문자열에 있는 숫자를 차례대로 더하려고 합니다. 이 때 "Z"가 나오면 바로 전에 더했던 숫자를 뺀다는 뜻입니다. 숫자와 "Z"로 이루어진 문자열 <code>s</code>가 주어질 때, 머쓱이가 구한 값을 return 하도록 solution 함수를 완성해보세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>s</code>의 길이 ≤ 200</li>
<li>-1,000 &lt; <code>s</code>의 원소 중 숫자 &lt; 1,000</li>
<li><code>s</code>는 숫자, "Z", 공백으로 이루어져 있습니다.</li>
<li><code>s</code>에 있는 숫자와 "Z"는 서로 공백으로 구분됩니다.</li>
<li>연속된 공백은 주어지지 않습니다.</li>
<li>0을 제외하고는 0으로 시작하는 숫자는 없습니다.</li>
<li><code>s</code>는 "Z"로 시작하지 않습니다.</li>
<li><code>s</code>의 시작과 끝에는 공백이 없습니다.</li>
<li>"Z"가 연속해서 나오는 경우는 없습니다.</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>s</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>"1 2 Z 3"</td>
<td>4</td>
</tr>
<tr>
<td>"10 20 30 40"</td>
<td>100</td>
</tr>
<tr>
<td>"10 Z 20 Z 1"</td>
<td>1</td>
</tr>
<tr>
<td>"10 Z 20 Z"</td>
<td>0</td>
</tr>
<tr>
<td>"-1 -2 -3 Z"</td>
<td>-3</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>본문과 동일합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>10 + 20 + 30 + 40 = 100을 return 합니다.</li>
</ul>

<p>입출력 예 #3</p>

<ul>
<li>"10 Z 20 Z 1"에서 10 다음 Z, 20 다음 Z로 10, 20이 지워지고 1만 더하여 1을 return 합니다.</li>
</ul>

<p>입출력 예 #4, #5</p>

<p>설명 생략</p>

<hr>

<p>※ 공지 - 2022년 11월 30일 제한사항 및 테스트 케이스가 수정되었습니다.</p>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges <br><br>

<hr>

## 🎁 나의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/7ba4eb0f-d12b-455a-9aab-02277d47ac27) <br>
-> 문자열을 공백으로 분리한다. 그리고 배열의 길이만큼 반복문을 돌면서, 'Z' 이면 그 이전 값을 answer에서 빼고, 그렇지 않으면 answer에 더해주고 마지막에 answer값을 반환해준다. <br><br>

## ⭕ 다른 사람의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/541d235f-4002-49be-9ac3-cb6bd3301a23) <br>
-> 스택으로 처리하였다. Z면 그 전꺼를 pop하고, 그렇지 않으면push해주었다. 반복문으로 forEach 사용하는 것도 알아보자!  <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/081a2979-62d6-4900-8627-3ff6a0b5f3b4) <br>
-> 여기서도 pop과 push를 활용하였다. 위와 같은 풀이이지만, 조금씩 코드 작성 방법이 달랐다.  <br><br>

## ✔️ What I learned: <br> 
- js에도 pop과 push 함수가 있다는것!!! <br>
- 배열에서 특정 몇 개의 값만 더하고 그런 알고리즘에선 스택을 생각해볼 수 있다는 것!! forEach문 사용하는 것 연습하기기
