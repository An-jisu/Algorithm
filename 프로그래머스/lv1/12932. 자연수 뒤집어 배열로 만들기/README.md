# [level 1] 자연수 뒤집어 배열로 만들기 - 12932 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/12932) 

### 성능 요약

메모리: 10.4 MB, 시간: 0.03 ms

### 구분

코딩테스트 연습 > 연습문제

### 채점결과

Empty

### 문제 설명

<p>자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.</p>

<h5>제한 조건</h5>

<ul>
<li>n은 10,000,000,000이하인 자연수입니다.</li>
</ul>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>n</th>
<th>return</th>
</tr>
</thead>
        <tbody><tr>
<td>12345</td>
<td>[5,4,3,2,1]</td>
</tr>
</tbody>
      </table>

> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges  <br><br>

<hr>

## ⭕ 다른 사람의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/4734f706-98d0-4fb1-94a3-fc33d9da882c) <br>
-> 나는 인덱싱을 활용하여 끝에서부터 접근하게끔 하였는데, 여기서는 reversed함수를 이용하여 하나씩 int로 바꿔주고 그 값을 list에 담아 반환하였다. 
