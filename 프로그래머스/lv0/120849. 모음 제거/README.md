# [level 0] 모음 제거 - 120849 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120849) 

### 성능 요약

메모리: 10.2 MB, 시간: 0.01 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

<br/>정확성: 100.0<br/>합계: 100.0 / 100.0

### 문제 설명

<p>영어에선 a, e, i, o, u 다섯 가지 알파벳을 모음으로 분류합니다. 문자열 <code>my_string</code>이 매개변수로 주어질 때 모음을 제거한 문자열을 return하도록 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li><code>my_string</code>은 소문자와 공백으로 이루어져 있습니다.</li>
<li>1 ≤ <code>my_string</code>의 길이 ≤ 1,000</li>
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
<td>"bus"</td>
<td>"bs"</td>
</tr>
<tr>
<td>"nice to meet you"</td>
<td>"nc t mt y"</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>"bus"에서 모음 u를 제거한 "bs"를 return합니다.</li>
</ul>

<p>입출력 예 #1</p>

<ul>
<li>"nice to meet you"에서 모음 i, o, e, u를 모두 제거한 "nc t mt y"를 return합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges <br><br>

<hr>

## 👑 나의 풀이: <br>
-> 문자열의 요소들에 하나씩 접근하면서, if문을 활용하여 만약 모음이면 삭제하도록 하였다. 그런데, replace함수는 문자열을 직접적으로 바꿔주는 것이 아닌, replace한 값을 반환해주는 함수이므로 반환값을 저장할 변수를 선언해주거나 해야한다. <br><br>

## ⭕ 다른 사람의 풀이: <br>
![image](https://user-images.githubusercontent.com/70849122/223010276-f04fd2c5-556e-4287-b910-871686c79073.png) <br>
-> 반대로, 모음에 속하지 않는 것들을 출력하는 형태로 코드를 짜도 된다.!! return문에 for문과 if문을 쓰는 코드 익히기<br>
![image](https://user-images.githubusercontent.com/70849122/223010313-8241c330-b880-4771-aa5e-4f43bd0b18d5.png) <br>
-> replace함수는 첫번째 꺼 뿐만 아니고, 해당되는 것을 모두 삭제해주는 함수라는 것!! <br>

## ✔ What I learned: <br>
- replace함수는 반환값을 가지고 있으며, 첫번째꺼 하나만 바꿔주는 것이 아닌 해당하는 문자를 모두 바꿔줄 수 있음!! <br>
