# [level 0] 양꼬치 - 120830 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120830?language=javascript) 

### 성능 요약

메모리: 33.4 MB, 시간: 0.03 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

Empty

### 문제 설명

<p>머쓱이네 양꼬치 가게는 10인분을 먹으면 음료수 하나를 서비스로 줍니다. 양꼬치는 1인분에 12,000원, 음료수는 2,000원입니다. 정수 <code>n</code>과 <code>k</code>가 매개변수로 주어졌을 때, 양꼬치 <code>n</code>인분과 음료수 <code>k</code>개를 먹었다면 총얼마를 지불해야 하는지 return 하도록 solution 함수를 완성해보세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>0 &lt; <code>n</code> &lt; 1,000</li>
<li>n / 10 ≤ <code>k</code> &lt; 1,000</li>
<li>서비스로 받은 음료수는 모두 마십니다.</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>n</th>
<th>k</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>10</td>
<td>3</td>
<td>124,000</td>
</tr>
<tr>
<td>64</td>
<td>6</td>
<td>768,000</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>10인분을 시켜 서비스로 음료수를 하나 받아 총 10 * 12000 + 3 * 2000 - 1 * 2000 = 124,000원입니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>64인분을 시켜 서비스로 음료수를 6개 받아 총 64 * 12000 + 6 * 2000 - 6 * 2000 =768,000원입니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges  <br><br>

<hr>

## 😀 나의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/e76f5d74-ac64-4843-8cc3-d269b1ab6d50) <br>
-> 음료수의 갯수를 k에서 인분을 10으로 나눈 몫을 빼주어 곱해준다. 그러면, 무료로 받은 음료수의 갯수는 제외시키고 계산할 수 있게된다. <br><br>

## ⭕ 다른 사람의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/503bc134-baff-42c9-9305-2ebf1079b5a6) <br>
-> 틸트 문법을 활용한 풀이이다. '~~'는 Math.floor을 의미한다. <br> <br>

## ✔️ What I learned: <br>
- js 틸트 문법: ~~는 Math.floor를 의미하는 연산자라는 거 기억하자!!
