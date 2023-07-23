# [level 0] 배열 회전시키기 - 120844 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120844?language=javascript) 

### 성능 요약

메모리: 33.3 MB, 시간: 0.07 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

Empty

### 문제 설명

<p>정수가 담긴 배열 <code>numbers</code>와 문자열&nbsp;<code>direction</code>가 매개변수로 주어집니다. 배열 <code>numbers</code>의 원소를 <code>direction</code>방향으로 한 칸씩 회전시킨 배열을 return하도록 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>3 ≤ <code>numbers</code>의 길이 ≤ 20</li>
<li><code>direction</code>은 "left" 와 "right" 둘 중 하나입니다.</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>numbers</th>
<th>direction</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>[1, 2, 3]</td>
<td>"right"</td>
<td>[3, 1, 2]</td>
</tr>
<tr>
<td>[4, 455, 6, 4, -1, 45, 6]</td>
<td>"left"</td>
<td>[455, 6, 4, -1, 45, 6, 4]</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li><code>numbers</code> 가 [1, 2, 3]이고 <code>direction</code>이 "right" 이므로 오른쪽으로 한 칸씩 회전시킨 [3, 1, 2]를 return합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li><code>numbers</code> 가 [4, 455, 6, 4, -1, 45, 6]이고 <code>direction</code>이 "left" 이므로 왼쪽으로 한 칸씩 회전시킨 [455, 6, 4, -1, 45, 6, 4]를 return합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges <br><br>

<hr>

## 🎁 나의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/49cb7bfe-20f9-4348-9afa-4453b4d5a6e6) <br>
-> direction에 따라 right, left 함수를 호출하게끔 하였다. right 함수에서는 0부터 끝의 앞까지 요소들을 가져와서 answer에 넣고, 마지막 요소를 unshift함수를 활용하여 맨 앞에 추가하였다. left함수에서는 두번째 요소부터 마지막 요소까지 배열에 넣고, push함수로 첫번째 요소를 맨 마지막에 삽입해주었다. <br><br>

## ⭕ 다른 사람의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/4b23c4f5-f91a-4b2b-b5a4-a61c4afe9da6) <br>
-> 마지막 요소를 제거해서 unshift함수를 통해서 맨 앞에 넣어주었다. 새로운 배열을 만들 것 없이, numbers 배열에 처리해주었다. 그리고 left 회전 시에는, shift로 마지막 요소 제거해서, 맨 마지막에 넣어준다.  <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/d65cb554-0416-46a3-b5a6-aae2cb301cbb) <br>
-> right인 경우에는, 마지막 요소를 가져오고, 나머지는 slice 로 가져왔다. left인 경우에는 slice로 1부터 마지막꺼까지 가져오고, 마지막에는 첫번때 인덱스의 값을 넣어주었다. <br><br>

## ✔️ What I learned: <br>
<배열에 요소 추가><br>
1. push: 배열의 뒤에 추가<br>
2. unshift: 배열의 앞에 추가/ 앞의 요소 삭제: shift <br>
- js에서의 pop은 마지막 요소를 제거하고 반환하고, 파이썬은 제거하지 않고 반환한다. <br>
- js pop함수: 마지막 요소 제거 <br>
--> shift: 맨 앞 요소 제거/ unshift: 맨 앞에 추가/////pop: 맨 뒤 요소 제거/push: 맨 뒤에 추가 <br>
