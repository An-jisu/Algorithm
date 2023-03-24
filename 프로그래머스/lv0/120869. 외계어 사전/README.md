# [level 0] 외계어 사전 - 120869 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120869) 

### 성능 요약

메모리: 10 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

<br/>정확성: 100.0<br/>합계: 100.0 / 100.0

### 문제 설명

<p>PROGRAMMERS-962 행성에 불시착한 우주비행사 머쓱이는 외계행성의 언어를 공부하려고 합니다. 알파벳이 담긴 배열 <code>spell</code>과 외계어 사전 <code>dic</code>이 매개변수로 주어집니다. <code>spell</code>에 담긴 알파벳을 한번씩만 모두 사용한 단어가 <code>dic</code>에 존재한다면 1, 존재하지 않는다면 2를 return하도록 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li><code>spell</code>과 <code>dic</code>의 원소는 알파벳 소문자로만 이루어져있습니다.</li>
<li>2 ≤ <code>spell</code>의 크기 ≤ 10</li>
<li><code>spell</code>의 원소의 길이는 1입니다.</li>
<li>1 ≤ <code>dic</code>의 크기 ≤ 10</li>
<li>1 ≤ <code>dic</code>의 원소의 길이 ≤ 10</li>
<li><code>spell</code>의 원소를 모두 사용해 단어를 만들어야 합니다.</li>
<li><code>spell</code>의 원소를 모두 사용해 만들 수 있는 단어는 <code>dic</code>에 두 개 이상 존재하지 않습니다.</li>
<li><code>dic</code>과 <code>spell</code> 모두 중복된 원소를 갖지 않습니다.</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>spell</th>
<th>dic</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>["p", "o", "s"]</td>
<td>["sod", "eocd", "qixm", "adio", "soo"]</td>
<td>2</td>
</tr>
<tr>
<td>["z", "d", "x"]</td>
<td>["def", "dww", "dzx", "loveaw"]</td>
<td>1</td>
</tr>
<tr>
<td>["s", "o", "m", "d"]</td>
<td>["moos", "dzx", "smm", "sunmmo", "som"]</td>
<td>2</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>"p", "o", "s" 를 조합해 만들 수 있는 단어가 <code>dic</code>에 존재하지 않습니다. 따라서 2를 return합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>"z", "d", "x" 를 조합해 만들 수 있는 단어 "dzx"가 <code>dic</code>에 존재합니다. 따라서 1을 return합니다.</li>
</ul>

<p>입출력 예 #3</p>

<ul>
<li>"s", "o", "m", "d" 를 조합해 만들 수 있는 단어가 <code>dic</code>에 존재하지 않습니다. 따라서 2을 return합니다.</li>
</ul>

<hr>

<h5>유의사항</h5>

<ul>
<li>입출력 예 #3 에서 "moos", "smm", "som"도 "s", "o", "m", "d" 를 조합해 만들 수 있지만 <code>spell</code>의 원소를 모두 사용해야 하기 때문에 정답이 아닙니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges   <br><br>


<hr>

## 👑 나의 풀이: <br>
-> 중첩 반복문을 활용하였다. 일단, dic에 있는 문자열에 하나씩 접근하면서, spell 문자가 존재하면 count를 1 증가시킨다. 그리고, 그 count가 spell 문자열의 길이와 같으면, 그 문자들이 모두 문자열에 존재하므로 return 1 을 한다. 만약 그 조건을 만족하지 않으면, 반복문을 계속 반복하면서 반복문이 끝나면, 그 spell의 모든 문자를 포함하는 문자열이 없다는 뜻이므로, return 2를 한다. <br><br>

## ⭕ 다른 사람의 풀이: <br>
![image](https://user-images.githubusercontent.com/70849122/227460749-990d5419-3cb2-433f-9b0b-9461872c5ee5.png) <br>
-> 집합의 차집합을 활용하였다. 이런 특정 문자의 존재에 대한 문자는 집합을 통해서 풀 수 있다는 것!!!! <br>
![image](https://user-images.githubusercontent.com/70849122/227460818-08a4e345-d68a-4a10-95cd-d9874cf45ec5.png) <br>
-> 진짜 그 요소 하나하나가 존재하는 지 확인하는 것이 아니라, dic 리스트의 요소들에 하나씩 접근하면서, spell을 정렬한 것과 dic의 요소 하나를 정렬한 것의 값이 같으면 1을 반환하도록 하였다. <br><br>

## ✔ What I learned: <br>
-> 요소의 존재 문제!!!: 하나의 리스트에 있는 요소가 다른 리스트에 모두 존재하냐 이런 문제는 집합으로 풀 수 있음!! <
