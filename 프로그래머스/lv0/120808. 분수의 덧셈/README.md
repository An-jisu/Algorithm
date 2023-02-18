# [level 0] 분수의 덧셈 - 120808 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120808) 

### 성능 요약

메모리: 10.4 MB, 시간: 0.25 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

<br/>정확성: 100.0<br/>합계: 100.0 / 100.0

### 문제 설명

<p>첫 번째 분수의 분자와 분모를 뜻하는 <code>numer1</code>, <code>denom1</code>, 두 번째 분수의 분자와 분모를 뜻하는 <code>numer2</code>, <code>denom2</code>가 매개변수로 주어집니다. 두 분수를 더한 값을 기약 분수로 나타냈을 때 분자와 분모를 순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>0 &lt;<code>numer1</code>, <code>denom1</code>,&nbsp;<code>numer2</code>, <code>denom2</code> &lt; 1,000</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>numer1</th>
<th>denom1</th>
<th>numer2</th>
<th>denom2</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>1</td>
<td>2</td>
<td>3</td>
<td>4</td>
<td>[5, 4]</td>
</tr>
<tr>
<td>9</td>
<td>2</td>
<td>1</td>
<td>3</td>
<td>[29, 6]</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>1 / 2 + 3 / 4 = 5 / 4입니다. 따라서 [5, 4]를 return 합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>9 / 2 + 1 / 3 = 29 / 6입니다. 따라서 [29, 6]을 return 합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges

<hr><br><br>

## 🎁 나의 코드와 풀이: <br>
-> 나는 파이썬의 라이브러리나 모듈들이 아는 게 많이 없다.따라서 직접 기약분수로 약분을 해주는 부분에서 코드에 대한 고민이 많았다. 
처음부터 분모들의 최소공배수로 통분하는 것을 코드로 짜는 것은 복잡해질 것이라고 판단되어, 일단은 두 분모를 모두 곱하는 통분을 하고자 위와 같이 res_son, res_parent를 생성하였다.
-> 그 후, 기약분수로 만드는 과정에서 분모와 분자중 작은값까지만 검사해서 약분을 하면 된다고 판단하였다.
-> 처음에는 for문을 2부터 res+1까지 반복하는 것으로 코드를 짰다. 하지만 생각해보니 4로 나눠지는 값(20/24)의 경우에는 2로 한 번 나눈 후, 2로 한 번더 나누어 줘야하는데, 2로 한 번 나눈 후에는 다음 i값인 3으로 넘어가게 된다. 따라서, 이런 예외를 처리하는 방법을 고민해보았다.
-> 2를 2번이 아닌 4로 먼저 나누면 한 번에 문제가 해결될 것 같다고 판단하였고, 큰 수부터 거꾸로 나누어보도록 코드를 다시 설계하였다.
-> 그리고 answer에 리스트로 반한하였다. <br>


## ⭕ 다른 사람들의 풀이:
1. **math 라이브러리**를 import 하여 gcd (최대공약수)함수 사용 가능!/ lcm 함수: 최소 공배수
![](https://velog.velcdn.com/images/asj1966/post/35608c54-592a-49ee-a77a-101fa544846f/image.png)

2. **fraction 모듈** 통해 분모 문자 형태로 만들 수 있음/ numerator를 통해 분자 알 수 있고, denominator를 통해 분모알 수 있음
![](https://velog.velcdn.com/images/asj1966/post/7a73e3f0-e42d-4b6f-919a-b595f8ac2eca/image.png) <br>


## 👍 What I learned
& 파이썬의 분수를 구하는 fraction모듈, 최대공약수 최소공배수 구하는 함수에 대해서 추가로 알게되었다. 또한, 예외를 처리하는 방법에 대한 고민을 해보았고, 그것을 바탕으로 코드를 수정하였다.
