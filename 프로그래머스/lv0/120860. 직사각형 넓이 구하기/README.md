# [level 0] 직사각형 넓이 구하기 - 120860 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120860?language=javascript) 

### 성능 요약

메모리: 33.5 MB, 시간: 1.88 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

Empty

### 문제 설명

<p>2차원 좌표 평면에 변이 축과 평행한 직사각형이 있습니다. 직사각형 네 꼭짓점의 좌표 [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]가 담겨있는 배열 <code>dots</code>가 매개변수로 주어질 때, 직사각형의 넓이를 return 하도록 solution 함수를 완성해보세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li><code>dots</code>의 길이 = 4</li>
<li><code>dots</code>의 원소의 길이 = 2</li>
<li>-256 &lt; <code>dots[i]</code>의 원소 &lt; 256</li>
<li>잘못된 입력은 주어지지 않습니다.</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>dots</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>[[1, 1], [2, 1], [2, 2], [1, 2]]</td>
<td>1</td>
</tr>
<tr>
<td>[[-1, -1], [1, 1], [1, -1], [-1, 1]]</td>
<td>4</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>좌표 [[1, 1], [2, 1], [2, 2], [1, 2]] 를 꼭짓점으로 갖는 직사각형의 가로, 세로 길이는 각각 1, 1이므로 직사각형의 넓이는 1 x 1 = 1입니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>좌표 [[-1, -1], [1, 1], [1, -1], [-1, 1]]를 꼭짓점으로 갖는 직사각형의 가로, 세로 길이는 각각 2, 2이므로 직사각형의 넓이는 2 x 2 = 4입니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges <br><br>

<hr>

## 🎁 나의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/f8eca006-f546-4200-b6f6-5a2f8125042a) <br>
-> 좌표가 순서대로 되어있는 게 아닐 수도 있으므로 첫 번째 좌표를 기준으로 x값이 같으면 h값을 구했고, y값이 같으면 w를 구했다. <br><br>

## ⭕ 다른 사람의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/34376ecd-7bc9-4c19-b0b7-6f57b4a848b9) <br>
-> x와 y는 2가지 값 씩만 존재한다. 따라서, x와 y값의 최댓값과 최솟값의 차이를 구해서 곱한다. 최대 최솟값 구할 때, ... 연산자를 이용해서 값을 가져와야 한다는 것<br><br>

## ✔️ What I learned: <br> 
- js 절댓값 라이브러리 함수: Math.abs() <br>
<변수> <br>
- var: 전역범위, 함수범위, 업데이트 및 재선언 가능, 호이스팅-undefiend<br>
- let: 블록범위, 업데이트 가능하지만 재선언 불가능, 호이스팅-error<br>
- const: 상수 <br>
-> 주로 var 변수를 사용하자!
