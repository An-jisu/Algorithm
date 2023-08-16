# [level 0] 저주의 숫자 3 - 120871 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120871?language=javascript) 

### 성능 요약

메모리: 33.5 MB, 시간: 0.12 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

Empty

### 문제 설명

<p>3x 마을 사람들은 3을 저주의 숫자라고 생각하기 때문에 3의 배수와 숫자 3을 사용하지 않습니다. 3x 마을 사람들의 숫자는 다음과 같습니다.</p>
<table class="table">
        <thead><tr>
<th>10진법</th>
<th>3x 마을에서 쓰는 숫자</th>
<th>10진법</th>
<th>3x 마을에서 쓰는 숫자</th>
</tr>
</thead>
        <tbody><tr>
<td>1</td>
<td>1</td>
<td>6</td>
<td>8</td>
</tr>
<tr>
<td>2</td>
<td>2</td>
<td>7</td>
<td>10</td>
</tr>
<tr>
<td>3</td>
<td>4</td>
<td>8</td>
<td>11</td>
</tr>
<tr>
<td>4</td>
<td>5</td>
<td>9</td>
<td>14</td>
</tr>
<tr>
<td>5</td>
<td>7</td>
<td>10</td>
<td>16</td>
</tr>
</tbody>
      </table>
<p>정수 <code>n</code>이 매개변수로 주어질 때, <code>n</code>을 3x 마을에서 사용하는 숫자로 바꿔 return하도록 solution 함수를 완성해주세요.</p>

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
<td>15</td>
<td>25</td>
</tr>
<tr>
<td>40</td>
<td>76</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>15를 3x 마을의 숫자로 변환하면 25입니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>40을 3x 마을의 숫자로 변환하면 76입니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges <br><br>

<hr>

## 🎁 나의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/e1f44148-4b3d-4942-93c9-a03622d742ea) <br>
-> n만큼씩 반복하면서, answer에 1씩 더 해준다. 그런데 그 값이 3의 배수이거나, 3을 포함하고 있다면 answer에 1을 더 더해준다. <br><br>

## ⭕ 다른 사람의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/d897fc1b-3549-4073-99aa-f215dc886edc) <br>
-> n크기의 3배짜리 배열을 생성한 후, 각각 1부터 map을 통해 넣어준다. 그리고, 3의 배수이거나 3을 포함하는 수를 제외하고 filtering 해준다. 그리고 n-1번째 값을 반환해준다. <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/665be45e-4e91-4666-8c1c-416a5643f851) <br>
<br>

## ✔️ What I learned: <br>
- 특정 규칙이 있는 배열의 값들만 남기고 싶으면, 배열 생성해서 값 담고 filtering!!!! 값들의 특정 규칙은 배열의 filtering을 통해서 해결해보자
