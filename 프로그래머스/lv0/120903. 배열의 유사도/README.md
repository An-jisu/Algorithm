# [level 0] 배열의 유사도 - 120903 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120903) 

### 성능 요약

메모리: 33.5 MB, 시간: 0.04 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

Empty

### 문제 설명

<p>두 배열이 얼마나 유사한지 확인해보려고 합니다. 문자열 배열 <code>s1</code>과 <code>s2</code>가 주어질 때 같은 원소의 개수를 return하도록 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>s1</code>, <code>s2</code>의 길이 ≤ 100</li>
<li>1 ≤ <code>s1</code>, <code>s2</code>의 원소의 길이 ≤ 10</li>
<li><code>s1</code>과 <code>s2</code>의 원소는 알파벳 소문자로만 이루어져 있습니다</li>
<li><code>s1</code>과 <code>s2</code>는 각각 중복된 원소를 갖지 않습니다.</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>s1</th>
<th>s2</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>["a", "b", "c"]</td>
<td>["com", "b", "d", "p", "c"]</td>
<td>2</td>
</tr>
<tr>
<td>["n", "omg"]</td>
<td>["m", "dot"]</td>
<td>0</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>"b"와 "c"가 같으므로 2를 return합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>같은 원소가 없으므로 0을 return합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges <br><br>

<hr>

## 🎁 나의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/3616dd5d-bc3e-43a3-ac38-d6df5251dfa1) <br>
-> 중복되는 수를 세기 위해, 두 배열을 합친 것의 길이에서 set으로 중복제거 해준 것의 길이를 빼주면, 중복되는 것의 갯수를 구할 수 있다. <br><br>

## ⭕ 다른 사람의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/edfc076b-83a7-425b-ac18-84f075619197) <br>
-> 아주 쉽게 s1에서 s2에 존재하는 것만 filter해주면 아주 간단하게 해결 가능!! 나도 처음에 filter로 하는 풀이를 생각했다. <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/3e4906ca-9114-4ff0-8d67-944103985190) <br>
-> 나는 2개의 배열을 합치는 것을 s1+','+s2로 처리하였는데, 더 간단한 방법이 있었다. 그렇게, set으로 바꾸고 Array.from으로 배열로 바꿔주었다. 그리고 그 중복된 갯수를 구해진 것! 나와 같은 풀이 방법이지만, 코드 짜는 방법이 조금 달랐다. 라이브러리 사용이나 그런 것들. <br><br> 

## ✔️ What I learned: <br> 
- js에서 2개의 배열 합치는 법 [...arr1, ...arr2] <br>
- 배열로 바꾸는 것: Array.from ()
