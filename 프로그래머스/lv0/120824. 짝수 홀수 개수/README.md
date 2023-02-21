# [level 0] 짝수 홀수 개수 - 120824 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120824) 

### 성능 요약

메모리: 10.1 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

<br/>정확성: 100.0<br/>합계: 100.0 / 100.0

### 문제 설명

<p>정수가 담긴 리스트&nbsp;<code>num_list</code>가 주어질 때, <code>num_list</code>의 원소 중 짝수와 홀수의 개수를 담은 배열을 return 하도록 solution 함수를 완성해보세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>num_list</code>의 길이 ≤ 100</li>
<li>0 ≤ <code>num_list</code>의 원소 ≤ 1,000</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>num_list</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>[1, 2, 3, 4, 5]</td>
<td>[2, 3]</td>
</tr>
<tr>
<td>[1, 3, 5, 7]</td>
<td>[0, 4]</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>[1, 2, 3, 4, 5]에는 짝수가 2, 4로 두 개, 홀수가 1, 3, 5로 세 개 있습니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>[1, 3, 5, 7]에는 짝수가 없고 홀수가 네 개 있습니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges <br><br>

<hr>

## 👑 나의 풀이: <br>
-> 새로운 변수를 2개 만들어서, 조건문을 사용하여 홀수, 짝수에 따라 개수를 증가시켜주었다. <br><br>

## ⭕ 다른 사람의 풀이: <br> 
![](https://velog.velcdn.com/images/asj1966/post/d4b8c0c3-e703-4782-8241-514636abd7c8/image.png)<br>
-> 나머지를 인덱싱으로 활용하였다. 나의 풀이와 같이 괜히 변수를 더 만들어서 더 많은 메모리를 차지할 필요가 없다는 것 <br> 
![](https://velog.velcdn.com/images/asj1966/post/9977a799-e456-4ecb-85ca-c9f0d89a4925/image.png)<br>
![](https://velog.velcdn.com/images/asj1966/post/5eec0709-1145-4b28-a97b-fce94dd2f4f5/image.png)<br><br>

## ✔ What I learned: <br>
-> 코드를 짤 때, 변수와 같은 것들을 최소화하여 메모리를 줄일 수 있는 방향으로 코드를 생각해보자!

