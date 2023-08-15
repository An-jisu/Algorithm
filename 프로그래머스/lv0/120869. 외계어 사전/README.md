# [level 0] 외계어 사전 - 120869 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120869?language=javascript) 

### 성능 요약

메모리: 33.4 MB, 시간: 0.07 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

Empty

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


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges  <br><br>

<hr>

## 🎁 나의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/6264fba7-d6ac-4c3a-88cb-d9000d4e6f36) <br>
-> 일단, spell에 있는 요소들을 모두 한번씩만 포함하는 것을 찾아내야한다. 따라서, spell의 길이와 같은 문자열만을 filter를 통해서 남기고, 그 값들에 하나씩 접근하였다. 그 값을 sort한 그 문자열 값이 spell을 sort하여 문자열로 바꾼 그 값이 같다면, 존재하는 것이므로 return 1 하게 하였다. 그리고 만약 같지 않다면 dic 다음요소로 넘어가게 한 후, 반복문이 끝날 때까지 return이 되지 않았다면 존재하지 않는 것이므로 2를 반환하게 하였다.  <br><br>

## ⭕ 다른 사람의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/033844ee-2812-4758-ab8a-7e20578dc4a8) <br>
-> spell을 정렬한 것, dic의 요소들 정렬한 것이 같은 것이 하나라도 있으면 1을 반환, 그렇지 않으면 2를 반환하도록 하였다. 나와 같은 풀이 방법이지만, some을 활용하여 좀 더 간단하게 나타냈다는 <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/0cb4069a-e0cc-44cd-acd1-f4311920b7af) <br>
-> 반례로는 spell=["p","o","s"], dic=["ppooss"] 가 있어서 사실 상 잘못된 풀이이다. spell에 있는 모든 요소들이 들어있는 것들만 flitering 한다. 그래서 filtering된 것이 없으면 length가 0이 되어, 존재하지 않는 것이므로 2를 반환한다. <br><br>

## ✔️ What I learned: <br> 
- sort함수를 문자열에선 사용할 수 없다는 것!! 문자열 sort하기 위해선, split("")로 배열로 바꾼 후, sort한 후, join으로 다시 묶어줄 수 있다. <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/202cbdb2-0af0-4ea2-8085-64d010f2a522) <br>
-> 배열로 바꿔주는 것을 이렇게 ...연산자로 접근해서 []담아서도 할 수 있다는 것!!! <br>
- every: 배열의 모든 요소가 어떤 조건을 충족하는 지 확인<br>
- some: 배열의 1개 요소라도 특정 조건을 충족하는 지 확인<br><br>
