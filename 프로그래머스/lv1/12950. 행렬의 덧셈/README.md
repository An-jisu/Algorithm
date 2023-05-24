# [level 1] 행렬의 덧셈 - 12950 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/12950) 

### 성능 요약

메모리: 22.9 MB, 시간: 57.28 ms

### 구분

코딩테스트 연습 > 연습문제

### 채점결과

Empty

### 문제 설명

<p>행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됩니다. 2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수, solution을 완성해주세요.</p>

<h5>제한 조건</h5>

<ul>
<li>행렬 arr1, arr2의 행과 열의 길이는 500을 넘지 않습니다.</li>
</ul>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>arr1</th>
<th>arr2</th>
<th>return</th>
</tr>
</thead>
        <tbody><tr>
<td>[[1,2],[2,3]]</td>
<td>[[3,4],[5,6]]</td>
<td>[[4,6],[7,9]]</td>
</tr>
<tr>
<td>[[1],[2]]</td>
<td>[[3],[4]]</td>
<td>[[4],[6]]</td>
</tr>
</tbody>
      </table>

> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges  <br><br>

<hr>

## ❤️ 문제 핵심: <br>
-> 각 행들의 합을 먼저 구해서 넣는 것이 핵심이었다<br><br>

## 😀 나의 풀이: <br>
행의 수 만큼 반복문을 돌면서, 행의 합을 tmp에 넣고, answer에 넣어주었다. c언어와는 달리 answer의 인덱스가 구체적으로 존재하지 않기 때문에, 이런식으로 풀어주었다. <br><br>

## ⭕ 다른 사람의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/d9557381-02f1-45e4-8fb3-2d55a064ac71) <br>
-> zip 함수를 활용하여, 행, 열의 요소에 접근하고 있다.!! <br><br>

## ✔️ What I learned: <br>
: 파이썬에서는 차례로 접근하는 것을 zip함수를 통해서 할 수 있다.
