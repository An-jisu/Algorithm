# [level 0] 숨어있는 숫자의 덧셈 (1) - 120851 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120851?language=javascript) 

### 성능 요약

메모리: 33.4 MB, 시간: 0.07 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

Empty

### 문제 설명

<p>문자열 <code>my_string</code>이 매개변수로 주어집니다. <code>my_string</code>안의 모든 자연수들의 합을 return하도록 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>my_string</code>의 길이&nbsp;≤ 1,000</li>
<li><code>my_string</code>은 소문자, 대문자 그리고 한자리 자연수로만 구성되어있습니다.</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>my_string</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>"aAb1B2cC34oOp"</td>
<td>10</td>
</tr>
<tr>
<td>"1a2b3c4d123"</td>
<td>16</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>"aAb1B2cC34oOp"안의 한자리 자연수는 1, 2, 3, 4 입니다. 따라서 1 + 2 + 3 + 4 = 10 을 return합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>"1a2b3c4d123Z"안의 한자리 자연수는 1, 2, 3, 4, 1, 2, 3 입니다. 따라서 1 + 2 + 3 + 4 + 1 + 2 + 3 = 16 을 return합니다.</li>
</ul>

<hr>

<h5>유의사항</h5>

<ul>
<li>연속된 숫자도 각각 한 자리 숫자로 취급합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges <br><br>

<hr>

## 🎁 나의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/30f4d5d7-3d5c-4284-93b6-7bec75d99c12) <br>
-> split을 통해 문자열의 각 요소들을 배열에 넣어주고, int형인 것만 filtering해준 이후(아직 문자열 형태임), map함수를 통해 숫자로 바꿔주었고, reduce함수를 통해서 값을 누적해서 더해주었다. <br><br>

## ⭕ 다른 사람의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/c13d906c-91ca-4cdb-bd1a-d349a61cc4ee) <br>
-> 정규식에서 '^'을 이용하여 숫자가 아닌 것은 모두 ''로 대체해주었고, split하여 배열에 담아주었다. 그리고 reduce함수를 통해서 누적해서 더해주었다. filter대신 replace 정규식을 통해서도 특정 문자들은 제거할 수 있다는 것 기억하자!! <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/8388ce6e-17be-44b9-9401-d6fc794cbc9c) <br>
-> reduce함수를 활용하여 누적해서 더 해주었다. <br><br>

## ✔️ What I learned: <br>
- js: 정규식 replace통해서 특정 문자 제거하기 (^연산자 기억하기)<br>
- 문자열 각각 분리해서 배열에: [...my_string], Array.from, split
