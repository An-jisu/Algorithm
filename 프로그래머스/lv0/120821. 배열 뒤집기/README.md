![image](https://github.com/An-jisu/Algorithm/assets/70849122/f47b868f-20a1-41a4-8b87-f58518f64ba1)# [level 0] 배열 뒤집기 - 120821 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120821?language=javascript) 

### 성능 요약

메모리: 33.5 MB, 시간: 0.03 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

Empty

### 문제 설명

<p>정수가 들어 있는 배열 <code>num_list</code>가 매개변수로 주어집니다. <code>num_list</code>의 원소의 순서를 거꾸로 뒤집은 배열을 return하도록 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>num_list</code>의 길이 ≤ 1,000</li>
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
<td>[5, 4, 3, 2, 1]</td>
</tr>
<tr>
<td>[1, 1, 1, 1, 1, 2]</td>
<td>[2, 1, 1, 1, 1, 1]</td>
</tr>
<tr>
<td>[1, 0, 1, 1, 1, 3, 5]</td>
<td>[5, 3, 1, 1, 1, 0, 1]</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li><code>num_list</code>가 [1, 2, 3, 4, 5]이므로 순서를 거꾸로 뒤집은 배열 [5, 4, 3, 2, 1]을 return합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li><code>num_list</code>가 [1, 1, 1, 1, 1, 2]이므로 순서를 거꾸로 뒤집은 배열 [2, 1, 1, 1, 1, 1]을 return합니다.</li>
</ul>

<p>입출력 예 #3</p>

<ul>
<li><code>num_list</code>가 [1, 0, 1, 1, 1, 3, 5]이므로 순서를 거꾸로 뒤집은 배열 [5, 3, 1, 1, 1, 0, 1]을 return합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges  <br><br>

<hr>

## 🎁 나의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/e1ee98b4-831e-4c85-9361-73563eeacef3) <br>
-> 반복문을 사용하여, push 함수를 사용하여 num_list의 끝 값부터 접근하면서 answer배열에 넣고 최종적으로 answer 배열을 return 하였다. <br><br>

## ⭕ 다른 사람의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/05c1c189-f13d-4cd1-8864-3715f9ec27cb) <br>
-> js에도 reverse 함수가 존재한다. reverse 함수로 함수를 뒤집어서 그대로 return 하였다. <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/613cd709-bb93-403d-a5e1-1af4625160da) <br>
-> answer에 앞쪽에 값 추가<br>


## ✔️ What I learned: <br>
<js 함수>
- push: 배열에 요소 넣기 <br>
- sort: 배열을 정렬 <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/9f62900b-2dfe-49ea-ab0b-2a8d6114a571) <br>
* 매개변수: compareFunction- 정렬 순서를 정의하는 함/ 생략 시, element들이 문자열로 취급되어 유니코드 순서대로 정렬/ 이 함수가 a, b 두개의 element를 파라미터로 입력받을 경우,
이 함수가 리턴하는 값이 0보다 작을 경우,  a가 b보다 앞에 오도록 정렬하고, 이 함수가 리턴하는 값이 0보다 클 경우, b가 a보다 앞에 오도록 정렬합니다. 만약 0을 리턴하면, a와 b의 순서를 변경하지 않습니다.<br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/33ecc5ea-db32-456f-b833-e2eaeb1d3e39) <br>
: 오름차순 정렬. 내림차순은 b-a <br>
- reverse: 원본 배열 거꾸로- 원본 배열 변<br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/a9b1b8e4-1361-47cd-b646-75e42edbec91) <br>
: 리턴되는 값만 변경-[...arr]는 arr배열을 복사한 값 <br>
- unshift: 새로운 요소를 배열의 맨 앞에 추가/ push는 뒤에 추가한다면 unshift는 앞 쪽에 추가 <br><br>

- forEach
