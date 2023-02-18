# [level 0] 배열 두배 만들기 - 120809 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120809) 

### 성능 요약

메모리: 10.2 MB, 시간: 0.17 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

<br/>정확성: 100.0<br/>합계: 100.0 / 100.0

### 문제 설명

<p>정수 배열 <code>numbers</code>가 매개변수로 주어집니다. <code>numbers</code>의 각 원소에 두배한 원소를 가진 배열을 return하도록 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>-10,000 ≤ <code>numbers</code>의 원소 ≤ 10,000</li>
<li>1 ≤ <code>numbers</code>의 길이 ≤ 1,000</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>numbers</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>[1, 2, 3, 4, 5]</td>
<td>[2, 4, 6, 8, 10]</td>
</tr>
<tr>
<td>[1, 2, 100, -99, 1, 2, 3]</td>
<td>[2, 4, 200, -198, 2, 4, 6]</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>[1, 2, 3, 4, 5]의 각 원소에 두배를 한 배열 [2, 4, 6, 8, 10]을 return합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>[1, 2, 100, -99, 1, 2, 3]의 각 원소에 두배를 한 배열 [2, 4, 200, -198, 2, 4, 6]을 return합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges



<hr>

## 🎁 나의 코드와 풀이: <br>
-> 배열의 각 요소를 일일히 2배하여, answer 리스트에 넣었다.

## ⭕ 다른 사람들의 풀이:
![](https://velog.velcdn.com/images/asj1966/post/e8847647-bb3a-4440-b44e-2bffe948e871/image.png)
-> 이와 같이 반복문 형태로도 나타낼 수 있음!!

## 👍 What I learned
& 내가 짠 코드는 직접 2배를 해주는 것으로 c언어에 익숙해진 풀이 방식이다. 리스트 문제의 경우 위와 같이 간단하게 끝낼 수 있음을 기억하자!!
