# [level 0] 영어가 싫어요 - 120894 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120894) 

### 성능 요약

메모리: 10.3 MB, 시간: 0.02 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

<br/>정확성: 100.0<br/>합계: 100.0 / 100.0

### 문제 설명

<p>영어가 싫은 머쓱이는 영어로 표기되어있는 숫자를 수로 바꾸려고 합니다. 문자열 <code>numbers</code>가 매개변수로 주어질 때, <code>numbers</code>를 정수로 바꿔 return 하도록 solution 함수를 완성해 주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li><code>numbers</code>는 소문자로만 구성되어 있습니다.</li>
<li><code>numbers</code>는 "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" 들이 공백 없이 조합되어 있습니다.</li>
<li>1 ≤ <code>numbers</code>의 길이 ≤ 50</li>
<li>"zero"는 <code>numbers</code>의 맨 앞에 올 수 없습니다.</li>
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
<td>"onetwothreefourfivesixseveneightnine"</td>
<td>123456789</td>
</tr>
<tr>
<td>"onefourzerosixseven"</td>
<td>14067</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>"onetwothreefourfivesixseveneightnine"를 숫자로 바꾼 123456789를 return합니다.</li>
</ul>

<p>입출력 예 #1</p>

<ul>
<li>"onefourzerosixseven"를 숫자로 바꾼 14067를 return합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges <br><br>

<hr>

## 👑 나의 풀이: <br>
-> replace함수가 있는 문장에서 result에 replace한 값을 넣고, 다시 그 result를 대체하였어야 했는데 처음에 두 번째에 result 대신 numbers를 넣어서 결과가 제대로 도출되지 않았다!! 그래도 딕셔너리를 사용하는 건 잘했다 ㅎ <br><br>

## ⭕ 다른 사람![image](https://user-images.githubusercontent.com/70849122/224341913-e797841d-4a00-4042-abbe-bd56b187f32d.png)의 풀이: <br>
![image](https://user-images.githubusercontent.com/70849122/224341982-1f6423ea-9a3c-49ae-a2e2-86d00e1473c1.png) <br>
-> 위와 같이 numerate를 사용하는 것도 연습하기!!! 또, result 변수를 굳이 다시 안 만들어주고, numbers 변수로 해주었어도 된다는 것!! 내 코드가 좀 비효율적이었다 <br><br>

## ✔ What I learned: <br>
-> replace 함수는 반환받는 값이 있어야 한다는 것!!! 또, 이렇게 특정 무언가를 특정 무언가로 계속해서 바꿔주어야 하는 경우에는, 딕셔너리를 이용해서 반복문 사용해서 풀면 된다는 것!!!
