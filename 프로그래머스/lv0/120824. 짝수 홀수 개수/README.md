# [level 0] 짝수 홀수 개수 - 120824 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120824?language=javascript) 

### 성능 요약

메모리: 33.4 MB, 시간: 0.04 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

Empty

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

## 😀 나의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/7520d925-9d97-4495-97cc-3f1e7e03dec8) <br>
-> new Array를 통해 배열을 생성하고, 0으로 채웠다. num_list의 요소들에 대해 하나씩 접근하면서 그 값에 따라 배열의 값을 증가시켜 반환하였다. 반복문은 of를 사용해서 처리하였다. <br><br>

## ⭕ 다른 사람의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/555225b6-7bea-4827-87f5-50d7608865f6) <br>
-> 배열을 만드는 것은 똑같다. 결괏값이 2개로 나뉘는 경우에는 참과 거짓으로 판별하여 인덱스로 접근할 수 있다. <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/ecf62214-bc00-4e42-831b-77e5f8f4639f) <br>
-> filter 함수로 짝수 홀수 걸러주고, 그 길이값을 return 하였다. <br>
<br><br>

## ✔ What I learned: <br>
-> 배열에서 특수 값들만을 걸러내야 하는 경우, filter를 써주는 것 연습하자!!! <br><br>
