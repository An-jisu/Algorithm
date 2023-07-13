# [level 0] 문자열 뒤집기 - 120822 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120822?language=javascript) 

### 성능 요약

메모리: 33.4 MB, 시간: 0.04 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

Empty

### 문제 설명

<p>문자열 <code>my_string</code>이 매개변수로 주어집니다. <code>my_string</code>을 거꾸로 뒤집은 문자열을 return하도록 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>my_string</code>의 길이 ≤ 1,000</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>my_string</th>
<th>return</th>
</tr>
</thead>
        <tbody><tr>
<td>"jaron"</td>
<td>"noraj"</td>
</tr>
<tr>
<td>"bread"</td>
<td>"daerb"</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li><code>my_string</code>이 "jaron"이므로 거꾸로 뒤집은 "noraj"를 return합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li><code>my_string</code>이 "bread"이므로 거꾸로 뒤집은 "daerb"를 return합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges <br><br>

<hr>

## 🎁 나의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/bd8fed27-413f-44a1-b7d0-4b6ea9771985) <br>
-> for문으로 my_string의 끝 글자부터 돌면서, answer에 더해주었고, 마지막에 반환하였다. <br><br>

## ⭕ 다른 사람의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/e9f45ee2-b816-4cec-a1a5-a257647016b6) <br>
-> split으로 문자열을 나누어주고, 거꾸로 하나씩 ''로 join해서 문자열로 반환해준다. <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/88757256-26a2-4e5f-8f30-7fde57207027) <br>
-> 나와 같은 풀이 방법인데, my_string[i] 대신 charAt(i)로 표현하였다. charAt 함수는 인덱싱과 같은 역할을 한다. 특정 인덱스에 위치하는 유니코드 단일문자를 반환한다. <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/13304eb5-b13c-4663-9725-be29bae6c3ef) <br>
-> 스프레드 연산자를 이용한 풀이이다. 문자열을 배열로 변환한 것이다. reverse로 배열을 역순으로 정렬하고, 다시 문자열로 나타내기 위해 join 해준다. <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/29233a62-8dcc-4e6c-b613-93c319b4274c) <br><br>

## ✔️ What I learned: <br>
- 문자열에 더할 땐, '+'연산자/ 배열에 요소 넣을 땐 push 함수 사용하기 <br>
- js에도 reverse, join, split 함수 있다는것 <br>
- 스프레드 연산자 (...): 기존의 것을 건들이지 않고 유지하면서 새로운 것을 추가하는 것이다. <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/47765cd1-6504-43d6-991d-810a960e4459) <br>
