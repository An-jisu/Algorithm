# [level 0] 다음에 올 숫자 - 120924 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120924) 

### 성능 요약

메모리: 10.1 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

<br/>정확성: 100.0<br/>합계: 100.0 / 100.0

### 문제 설명

<p>등차수열 혹은 등비수열 <code>common</code>이 매개변수로 주어질 때, 마지막 원소 다음으로 올 숫자를 return 하도록 solution 함수를 완성해보세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>2 &lt; <code>common</code>의 길이 &lt; 1,000</li>
<li>-1,000 &lt; <code>common</code>의 원소 &lt; 2,000

<ul>
<li><code>common</code>의 원소는 모두 정수입니다.</li>
</ul></li>
<li>등차수열 혹은 등비수열이 아닌 경우는 없습니다.</li>
<li>등비수열인 경우 공비는 0이 아닌 정수입니다.</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>common</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>[1, 2, 3, 4]</td>
<td>5</td>
</tr>
<tr>
<td>[2, 4, 8]</td>
<td>16</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>[1, 2, 3, 4]는 공차가 1인 등차수열이므로 다음에 올 수는 5이다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>[2, 4, 8]은 공비가 2인 등비수열이므로 다음에 올 수는 16이다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges <br><br>

<hr>

## 👑 나의 풀이: <br>
-> 등차수열인 경우, 등비수열인 경우를 나눠서 생각해보았다. 등차수열인 경우에는 0-1번째의 차이와 1-2번째의 차이가 같으면, 마지막 숫자 인덱스 '-1'인 값에 그 차이를 더해서 반환하도록 하였다. 등비수열인 경우에는 0-1번째의 몫과 1-2번째의 몫이 같으면, 인덱스 '-1'인 곳의 값에 몫을 곱해서 반환하도록 하였다. <br><br>

## ⭕ 다른 사람의 풀이: <br>
![image](https://user-images.githubusercontent.com/70849122/231043063-1c75a2bc-5117-4d4a-bcdf-cd41afa610f9.png) <br>
-> 나랑 같은 풀이법이다. 하지만 여기서 인덱스의 요소에 접근하는 것을 간단히 하기 위하여 'a,b,c = common[:3]'으로 처리해준 것을 눈여겨 보자!! <br><br>

## ✔ What I learned: <br>
-> 파이썬에서는 마지막 요소에 인덱스 '-1'을 통해 접근할 수 있다는 것!<br>
-> 배열의 요소는 'a,b,c = common[:3]' 와 같이 변수에 값을 저장할 수 있다는 것!<br>
