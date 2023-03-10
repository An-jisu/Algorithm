# [level 0] 한 번만 등장한 문자 - 120896 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120896) 

### 성능 요약

메모리: 10.1 MB, 시간: 0.01 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

<br/>정확성: 100.0<br/>합계: 100.0 / 100.0

### 문제 설명

<p>문자열 <code>s</code>가 매개변수로 주어집니다. <code>s</code>에서 한 번만 등장하는 문자를 사전 순으로 정렬한 문자열을 return 하도록 solution 함수를 완성해보세요. 한 번만 등장하는 문자가 없을 경우 빈 문자열을 return 합니다.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>0 &lt; <code>s</code>의 길이 &lt; 1,000</li>
<li><code>s</code>는 소문자로만 이루어져 있습니다.</li>
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
<td>"abcabcadc"</td>
<td>"d"</td>
</tr>
<tr>
<td>"abdc"</td>
<td>"abcd"</td>
</tr>
<tr>
<td>"hello"</td>
<td>"eho"</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>"abcabcadc"에서 하나만 등장하는 문자는 "d"입니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>"abdc"에서 모든 문자가 한 번씩 등장하므로 사전 순으로 정렬한 "abcd"를 return 합니다.</li>
</ul>

<p>입출력 예 #3</p>

<ul>
<li>"hello"에서 한 번씩 등장한 문자는 "heo"이고 이를 사전 순으로 정렬한 "eho"를 return 합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges  <br><br>

<hr>

## 👑 나의 풀이: <br>
-> 문자열의 문자에 하나씩 접근하면서, count한 값이 1개이면, answer 문자열에 넣도록 하였다. 그런데, 처음에 ''.join을 해주지 않았더니 문자열 형태로 반환되어서 문자열 형태로 바꿔주어야 했다. 그 이유를 인터넷에 검색해보니, sorted 함수는 문자열을 알파벳 순으로 정렬하면, 리스트 형태로 반환해준다는 것!!! <br><br>

## ⭕ 다른 사람의 풀이: <br>
![image](https://user-images.githubusercontent.com/70849122/224207289-afed2aec-0189-48b6-9e8d-c9601b53e1b0.png) <br>
-> 이렇게 한 줄로 for 문 if문 모두 써서 반환하는 연습하자!!<br><br>

## ✔ What I learned: <br>
-> 숫자를 정렬할 때는, answer.sort() 이런식으로 하지만, 문자열을 정렬할 때는 sort(answer) 이런식으로! <br>
또한, sorted함수로 문자열을 정렬하면, 리스트 형태로 반환해준다는 것<br>
