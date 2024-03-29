# [level 0] 각도기 - 120829 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120829?language=javascript) 

### 성능 요약

메모리: 33.3 MB, 시간: 0.03 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

Empty

### 문제 설명

<p>각에서 0도 초과 90도 미만은 예각, 90도는 직각, 90도 초과 180도 미만은 둔각 180도는 평각으로 분류합니다. 각 <code>angle</code>이 매개변수로 주어질 때 예각일 때 1, 직각일 때 2, 둔각일 때 3, 평각일 때 4를 return하도록 solution 함수를 완성해주세요.</p>

<ul>
<li>예각 : 0 &lt; <code>angle</code> &lt; 90</li>
<li>직각 : <code>angle</code> = 90</li>
<li>둔각 : 90 &lt; <code>angle</code> &lt; 180</li>
<li>평각 : <code>angle</code> = 180</li>
</ul>

<hr>

<h5>제한사항</h5>

<ul>
<li>0 &lt; <code>angle</code> ≤ 180</li>
<li><code>angle</code>은 정수입니다.</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>angle</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>70</td>
<td>1</td>
</tr>
<tr>
<td>91</td>
<td>3</td>
</tr>
<tr>
<td>180</td>
<td>4</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li><code>angle</code>이 70이므로 예각입니다. 따라서 1을 return합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li><code>angle</code>이 91이므로 둔각입니다. 따라서 3을 return합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li><code>angle</code>이 180이므로 평각입니다. 따라서 4를 return합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges  <br><br>

<hr>

## 😀 나의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/f7de8c0f-aef8-4854-99dd-87e42fd50d06) <br>
-> 조건문을 활용해서 if, else if, else로 처리하였다.<br><br>

## ⭕ 다른 사람의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/10e62b81-d519-4828-aa46-62880548f662) <br>
-> filter함수로 거르고, length로 구해주었다.<br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/05f3bcb5-62e7-4878-8323-4e8a159207fd) <br>
-> 삼항 연산자를 이용하여 분기를 처리하였다. <br><br>


## ✔  What I learned: <br> 
- js에서의 조건문은 elif아니고 else if 이다.<br>
- js에서는 and연산자를 &&이렇게 표현하였다. <br>
- 특정한 값만 남기는 것, 제거하는 것, 분기하는 건 filter함수로 쓸 수 있다!!<br>
- js에서는 조건문 보다는 삼항연산자로 쓰는 것을 연습하자!! <br><br>
- js에서도 switch문을 사용할 수 있다        
