# [level 0] 짝수의 합 - 120831 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120831?language=javascript) 

### 성능 요약

메모리: 33.4 MB, 시간: 0.03 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

Empty

### 문제 설명

<p>정수 <code>n</code>이 주어질 때, <code>n</code>이하의 짝수를 모두 더한 값을 return 하도록 solution 함수를 작성해주세요.</p>

<hr>

<h5>제한사항</h5>

<p>0 &lt; <code>n</code> ≤ 1000</p>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>n</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>10</td>
<td>30</td>
</tr>
<tr>
<td>4</td>
<td>6</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li><code>n</code>이 10이므로 2 + 4 + 6 + 8 + 10 = 30을 return 합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li><code>n</code>이 4이므로 2 + 4 = 6을 return 합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges  <br><br>

<hr>

## 😀 나의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/4b152f0e-2b48-4c9f-8dd0-f7b95960ad52) <br>
-> 반복문을 통해 요소의 하나씩 접근하면서 짝수들만을 더해 return 해주었다. 뭔가 반복문 말고 라이브러리 사용해서는 풀 수 없을지... <br><br>

## ⭕ 다른 사람의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/de14111e-3674-499e-9258-c6c65f349b53) <br>
-> 메서드 체이닝으로 수행하였다. 배열을 만들어, 각각을 채우는데 map으로 +씩 더해주었다. 그리고 filter로 짝수만 걸러주고 reduce함수로 더해준다. 나도 처음에 reduce 함수로 더하는 것을 잘한 듯!!

## ✔️ What I leanred: <br>
-> 함수 여러 개 연결하는 것을 메서드 체이닝이라고 한다!!<br>
