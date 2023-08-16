# [level 0] k의 개수 - 120887 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120887?language=javascript) 

### 성능 요약

메모리: 38.9 MB, 시간: 9.08 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

Empty

### 문제 설명

<p>1부터 13까지의 수에서, 1은 1, 10, 11, 12, 13 이렇게 총 6번 등장합니다. 정수 <code>i</code>, <code>j</code>, <code>k</code>가 매개변수로 주어질 때, <code>i</code>부터 <code>j</code>까지 <code>k</code>가 몇 번 등장하는지 return 하도록 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>i</code> &lt; <code>j</code> ≤ 100,000</li>
<li>0 ≤ <code>k</code> ≤ 9</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>i</th>
<th>j</th>
<th>k</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>1</td>
<td>13</td>
<td>1</td>
<td>6</td>
</tr>
<tr>
<td>10</td>
<td>50</td>
<td>5</td>
<td>5</td>
</tr>
<tr>
<td>3</td>
<td>10</td>
<td>2</td>
<td>0</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>본문과 동일합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>10부터 50까지 5는 15, 25, 35, 45, 50 총 5번 등장합니다. 따라서 5를 return 합니다.</li>
</ul>

<p>입출력 예 #3</p>

<ul>
<li>3부터 10까지 2는 한 번도 등장하지 않으므로 0을 return 합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges <br><br>

<hr>

## 🎁 나의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/60c7dea8-6dc1-4654-ad50-89a5922872fa) <br>
-> j개 짜리 배열을 만들고, 값을 집어넣은 후, i보다 큰 값들만을 남겨두었다. 그리고 그것들을 join하고 split을 통해 하나하나 분리해준 후, k값만 남겨서 그 길이를 구했다.<br><br>

## ⭕ 다른 사람의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/a51cc7f1-a4fd-4bd4-a9f1-76759d932b94) <br>
-> 반복문을 통해, 범위 사이의 값을 문자열에 더해주었다. 그리고 k를 기준으로 split하여 -1을 해주었다. split의 여집합 이용한 풀이이다!!!!<br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/e8676422-61fc-4dbd-8c71-9d207d095e46) <br>
-> Array.from을 통해서도 배열로 바꿀 수 있다. from은 문자열을 문자 하나하나 분리하여, 배열에 요소를 넣어주는 것이다. <br><br>

# ✔️ What I learned: <br>
- join은 자동으로 문자열로 합쳐준다는 것! <br>
- 필터링은 문자열에선 불가능하고, 배열에서 할 수 있다는 것! <br>
- split의 여집합: 어떤 배열에서 k의 갯수를 구할 때, 그것을 기준으로 split하고 -1 해준 값 반환! 특정 값의 갯수 구할 때, 그 값을 기준으로 split하고 -1하여 구할 수 있다는 것 <br>
- 문자열의 요소들을 하나씩 배열에 넣어주고 싶을 때: Array.from()!! / split("")
