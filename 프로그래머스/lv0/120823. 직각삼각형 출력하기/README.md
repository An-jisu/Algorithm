# [level 0] 직각삼각형 출력하기 - 120823 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120823) 

### 성능 요약

메모리: 7.55 MB, 시간: 11.33 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

<br/>정확성: 100.0<br/>합계: 100.0 / 100.0

### 문제 설명

<p>"*"의 높이와 너비를 1이라고 했을 때, "*"을 이용해 직각 이등변 삼각형을 그리려고합니다.  정수 n 이 주어지면 높이와 너비가 n 인 직각 이등변 삼각형을 출력하도록 코드를 작성해보세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>n</code> ≤ 10</li>
</ul>

<hr>

<h5>입출력 예</h5>

<p>입력 #1</p>
<div class="highlight"><pre class="codehilite"><code>3
</code></pre></div>
<p>출력 #1</p>
<div class="highlight"><pre class="codehilite"><code>*
**
***
</code></pre></div>
<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>n이 3이므로 첫째 줄에 * 1개, 둘째 줄에 * 2개, 셋째 줄에 * 3개를 출력합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges <br><br>

<hr>

## 👑 나의 풀이: <br>
-> c언어에서의 별 찍기 문제와 똑같이 생각하였다. 중첩 반복문을 활용하여 한 줄 씩 출력하였다. <br>
![](https://velog.velcdn.com/images/asj1966/post/441a93af-960d-4ac9-8170-fed7b3b854a1/image.png) <br>
-> 처음에는 위와 같이 코드를 짰는데, 한 줄의 요소들도 모두 개행이 적용되어 출력되는 것이다. 파이썬에서의 프린트는 개행이 적용되어 나온다는 것!!! 따라서 개행을 원하지 않는다면, 정정한 나의 코드와 같이 print('*', end="")와 같이 end를 작성해서, print가 완료된 후의 처리를 해주어야 함!!! <br>

## ⭕ 다른 사람의 풀이: <br>
![](https://velog.velcdn.com/images/asj1966/post/923f3164-4b47-4d65-b84f-25dabb7ec908/image.png) <br>
-> 단일 반복문을 활용하여, i번째 줄에 i개의 *이 출력되게 하였다.


## ✔ What I learned: <br>
!!!! 매우 중요하고 기본 적인 것!!!! <br>
<b> 파이썬에서의 print문은 기본적으로 개행을 포함하고 있다는 것!! 개행을 원하지 않는다면, end로 처리를 해줘야한다는 것!!!! 
