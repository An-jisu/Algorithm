# [level 0] 약수 구하기 - 120897 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120897?language=javascript) 

### 성능 요약

메모리: 33.4 MB, 시간: 0.08 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

Empty

### 문제 설명

<p>정수 <code>n</code>이 매개변수로 주어질 때, <code>n</code>의 약수를 오름차순으로 담은 배열을 return하도록 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>n</code> ≤ 10,000</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>n</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>24</td>
<td>[1, 2, 3, 4, 6, 8, 12, 24]</td>
</tr>
<tr>
<td>29</td>
<td>[1, 29]</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>24의 약수를 오름차순으로 담은 배열 [1, 2, 3, 4, 6, 8, 12, 24]를 return합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>29의 약수를 오름차순으로 담은 배열 [1, 29]를 return합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges <br><br>

<hr>

## 🎁 나의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/3e3e2989-3bd5-418c-9bd4-48aaea5d69fe) <br>
-> n까지 반복문을 돌면서, n이 i로 나누어떨어지면, 그 값을 answer에 넣게 하였고, 마지막에는 answer를 sort한 값을 반환하였다. <br>

## ⭕ 다른 사람의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/5282ca15-8fe9-474b-bf75-1cc824ded5f9) <br>
-> n까지의 숫자를 배열을 만들어 채우고, n으로 그 값을 나누었을 때 나누어 떨어지는 값들만 filter하게 하였다. n까지의 값을 순차적으로 접근하므로 딱히 sort함수를 사용할 필요가 없다는 것!! <br><br>
