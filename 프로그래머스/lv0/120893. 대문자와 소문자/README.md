# [level 0] 대문자와 소문자 - 120893 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120893?language=javascript) 

### 성능 요약

메모리: 33.5 MB, 시간: 0.30 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

Empty

### 문제 설명

<p>문자열 <code>my_string</code>이 매개변수로 주어질 때, 대문자는 소문자로 소문자는 대문자로 변환한 문자열을 return하도록 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>my_string</code>의 길이 ≤ 1,000</li>
<li><code>my_string</code>은 영어 대문자와 소문자로만 구성되어 있습니다.</li>
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
<td>"cccCCC"</td>
<td>"CCCccc"</td>
</tr>
<tr>
<td>"abCdEfghIJ"</td>
<td>"ABcDeFGHij"</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>소문자는 대문자로 대문자는 소문자로 바꾼 "CCCccc"를 return합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>소문자는 대문자로 대문자는 소문자로 바꾼 "ABcDeFGHij"를 return합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges <br><br>

<hr>

## 🎁 나의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/b47529fe-6619-4ae1-8fda-c1d97937451f) <br>
-> a를 toUpperCase한 것이 a와 같다면 대문자라는 뜻이므로, map함수를 통해서 하나씩 검사하면서 대문자이면 toLowerCase함수를 통해 소문자로 바꾸고 answer에 더해주었고, 소문자이면 대문자로 바꿔서 answer에 더해주었다.<br><br>

## ⭕ 다른 사람의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/d1f08cf1-da71-40fe-a82b-fc969fc8f467) <br>
-> 나와 같은 풀이 방법이다. 그런데 여기서는 굳이 각 문자를 배열로 바꿔서 map으로 접근하지 않았고, for문을 통해서 하나씩 접근하였다. 또한, 대입을 위와 같이 넣으면 참과 거짓일 때 중복으로 answer+=을 넣어주지 않아도 된다는 것 <br><br>

## ✔️ What I learned: <br> 
- 대문자 소문자 변환: toUpperCase(), toLowerCase() <br>
- 어쨌튼, 조건문 대신 삼항연산자 쓰기!!!!! 화살표 함수!!!!! 반복문 보다 filter, reduce, map, .. 사용하는 것 연습하기. for문으로도 할 줄 알아야 함. js에만 있는 라이브러리 없이도 어느 언어든 호환가능하게!
