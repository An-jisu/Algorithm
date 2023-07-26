# [level 0] 369게임 - 120891 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120891?language=javascript) 

### 성능 요약

메모리: 33.5 MB, 시간: 0.05 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

Empty

### 문제 설명

<p>머쓱이는 친구들과 369게임을 하고 있습니다. 369게임은 1부터 숫자를 하나씩 대며 3, 6, 9가 들어가는 숫자는 숫자 대신 3, 6, 9의 개수만큼 박수를 치는 게임입니다. 머쓱이가 말해야하는 숫자 <code>order</code>가 매개변수로 주어질 때, 머쓱이가 쳐야할 박수 횟수를 return 하도록 solution 함수를 완성해보세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>order</code> ≤ 1,000,000</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>order</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>3</td>
<td>1</td>
</tr>
<tr>
<td>29423</td>
<td>2</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>3은 3이 1개 있으므로 1을 출력합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>29423은 3이 1개, 9가 1개 있으므로 2를 출력합니다.</li>
</ul>

<hr>

<p>※ 공지 - 2023년 03월 24일 테스트 케이스가 추가되었습니다. 기존에 제출한 코드가 통과하지 못할 수도 있습니다.</p>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges <br><br>

<hr>

## 🎁 나의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/84bfe13b-672e-49cc-869a-9b2992471bf4) <br>
-> string으로 바꾸고, split을 하여 한 글자씩 검사하면서 3,6,9인 수만 남기고, 그 배열의 길이를 구했다. 3으로 나누어떨어지느냐 logic으로 수행하였는데, 0인 경우를 생각하지 못해서 오류가 났다. <br><br> 

## ⭕ 다른 사람의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/fbd5115c-cd1a-4505-baf7-795cfbe1b7dc) <br>
-> order를 가져와서, 3,6,9가 있는 문자만 남기고 그 이외의 값은 모두 없앤다. 그리고 그 길이를 구해주었다. <br><br>

## ✔️ What I learned: <br> 
- js: 숫자를 string으로 바꾸기-> String(숫자)/ ''+숫자<br>
- match: 정규식에 매치되는 값을 배열로 반. 정규식 이용 시 같이 사용하는 함수!!<br>
- matchAll: g플래그가 없으면 타입에러<br>
