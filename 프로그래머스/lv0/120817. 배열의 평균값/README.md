# [level 0] 배열의 평균값 - 120817 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120817) 

### 성능 요약

메모리: 10 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

<br/>정확성: 100.0<br/>합계: 100.0 / 100.0

### 문제 설명

<p>정수 배열 <code>numbers</code>가 매개변수로 주어집니다. <code>numbers</code>의 원소의 평균값을 return하도록 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>0 ≤ <code>numbers</code>의 원소 ≤ 1,000</li>
<li>1 ≤ <code>numbers</code>의 길이 ≤ 100</li>
<li>정답의 소수 부분이 .0 또는 .5인 경우만 입력으로 주어집니다. </li>
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
<td>[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]</td>
<td>5.5</td>
</tr>
<tr>
<td>[89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]</td>
<td>94.0</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li><code>numbers</code>의 원소들의 평균 값은 5.5입니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li><code>numbers</code>의 원소들의 평균 값은 94.0입니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges <br>
<hr>

## 🎁 나의 풀이:<br>
-> 반복문을 통해 배열 요소들의 합을 구한 후, len으로 나눈 평균 값을 반환


## ⭕ 다른 사람들의 풀이: <br>
1. numpy의 사용<br>
![](https://velog.velcdn.com/images/asj1966/post/13e85241-60c9-46a1-96a1-02f9683cb78b/image.png)<br>
2. sum(numbers)/len(numbers)<br>
-> 반복문 사용없이, 파이썬에서는 바로 sum함수 사용 가능! <br><br>

## ✔ What I learned:<br>
-> 파이썬 numpy 라이브러리에는 평균을 구하는 mean 함수가 존재함

