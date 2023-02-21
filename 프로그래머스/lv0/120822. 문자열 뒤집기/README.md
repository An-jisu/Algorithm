# [level 0] 문자열 뒤집기 - 120822 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120822) 

### 성능 요약

메모리: 9.89 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

<br/>정확성: 100.0<br/>합계: 100.0 / 100.0

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

## 👑 나의 풀이: <br>
-> 굳이 배열을 뒤집지 않고, string을 거꾸로 하나씩 출력하였다. <br><br>

## ⭕ 다른 사람의 풀이: <br>
![](https://velog.velcdn.com/images/asj1966/post/101e2828-6ae8-4d1a-8b9d-7d3a5e2717f7/image.png)<br>
-> reversed() 함수를 이용하여, 문자열을 뒤집고, list로 만든 후, 다시 문자열로 만들어 반환하였다. <br><br>

## ✔ What I learned: <br>
-> 파이썬에서 문자열이나 리스트를 거꾸로 뒤집는 방법<br>
1. 문자열[::-1] <br>
2. list(reversed(문자열)) <br>
![](https://velog.velcdn.com/images/asj1966/post/d0ca42a3-5958-40f2-a734-3cbbdb79e493/image.png) <br>
-> reversed()함수에 list를 씌어주지 않으면, 아래와 같이 reversed()의 객체가 반환된다. <br>
![](https://velog.velcdn.com/images/asj1966/post/c25244fe-f105-49c2-9aaf-c7b96db1289c/image.png) <br>
- 리스트를 다시 문자열 형태로 띄어쓰기 없이 출력하려면 아래와 같이 ''로 join을 해주면 된다. <br>
![](https://velog.velcdn.com/images/asj1966/post/89be980e-f26a-4fca-96d3-bdacc91a79e4/image.png)


<br>
