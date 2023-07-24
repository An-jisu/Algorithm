# [level 0] 모음 제거 - 120849 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120849?language=javascript) 

### 성능 요약

메모리: 33.6 MB, 시간: 0.06 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

Empty

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

## 🎁 나의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/cdbef809-4d46-4a8a-aba5-8bc1515900ac) <br>
-> my_stirng 각 요소를 분리하여 split함수를 통해 배열에 넣고, answer에 없는 값들을 filter해주었다. 파이썬에서는 a not in answer라고 하면 되지만, js에서는 includes 함수를 사용해주어야 한다. <br><br>

## ⭕ 다른 사람의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/467378f4-da06-499f-9182-a4ea88fc4c0e) <br>
-> 정규식을 활용해 처리하였다. 정규식에 해당하면, ''로 replace하게끔 하였다. <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/d1677a30-186c-42d2-a567-b313e3eeeb20) <br>
-> 모음을 만나면 splice함수를 통해 원본 배열을 변경하게끔 처리하였다. 특정 범위 부분을 제거<br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/db69f839-1943-4573-b2d0-d58d716bfb06) <br>
-> 따로 answer 배열을 만들지 않고, 위와 같이 한줄로 처리할 수 있다. 또한, split대신 Array.from 함수를 사용할 수 있다.<br><br>


## ✔️ What I learned: <br> 
- replace: js에서도 replace함수가 존재한다. <br>
- js에서 특정 문자 제거: replace, splice, includes<br>
- 문자열 분리: split, Array.from<br>
