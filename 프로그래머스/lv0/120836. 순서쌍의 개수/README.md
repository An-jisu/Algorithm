# [level 0] 순서쌍의 개수 - 120836 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120836?language=javascript) 

### 성능 요약

메모리: 33.5 MB, 시간: 0.15 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

Empty

### 문제 설명

<p>순서쌍이란 두 개의 숫자를 순서를 정하여 짝지어 나타낸 쌍으로 (a, b)로 표기합니다. 자연수 <code>n</code>이 매개변수로 주어질 때 두 숫자의 곱이 <code>n</code>인 자연수 순서쌍의 개수를 return하도록 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ n ≤ 1,000,000</li>
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
<td>20</td>
<td>6</td>
</tr>
<tr>
<td>100</td>
<td>9</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li><code>n</code>이 20 이므로 곱이 20인 순서쌍은 (1, 20), (2, 10), (4, 5), (5, 4), (10, 2), (20, 1) 이므로 6을 return합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li><code>n</code>이 100 이므로 곱이 100인 순서쌍은 (1, 100), (2, 50), (4, 25), (5, 20), (10, 10), (20, 5), (25, 4), (50, 2), (100, 1) 이므로 9를 return합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges  <br><br>

<hr>

## 🎁 나의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/5cbdecbb-3832-4101-af06-9c1bb54c90a9) <br>
-> 제곱근 값 까지만 반복문을 돌면서, n의 약수의 갯수를 구하고 최종적으로 2를 곱한 값을 반환해주었다. 그런데 만약 n의 제곱근값의 int를 취한 후, 제곱한 값이 n과 같으면, 제곱수이므로 마지막에 1을 빼준다. (ex-10*10) 즉, 나는 제곱근값의 약수의 갯수로 답을 구했다. <br><br>

## ⭕ 다른 사람의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/2bbd97d2-2507-4909-85a5-16f2f0ee2006) <br>
-> 나와 같은 풀이 방법이다. 하지만, 1씩 더해주어 마지막에 2를 곱해준 것이 아닌, 처음부터 2씩 더해주었다. 그리고 마지막에는 삼항 연산자를 이용하여 만약 제곱근값이 int이면 100과 같은 제곱수이므로 1을 더한 값을 return한 것이다. 나는 제곱수인 경우를 판단해주는 것을 복잡하게 했는데, 그냥 제곱근 값이 정수인지 확인해보면 된다!! <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/7e741dc4-5af3-45ea-8e69-2974d3275e09) <br>
-> 내가 처음 생각한 풀이와 같다. 그냥 n까지 접근하면서, 그냥 나누어떨어지면 더해주었다. <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/76ad0036-98e9-4bc4-bbf6-5d1d3c88c54f) <br>
-> 반복문으로 n까지 접근해주는 부분을 for문 없이 배열로 1을 채워주고, 1부터 n까지 접근하는 것 배열에 1로 채운 후, 인덱스 값을 더해주었다. 그리고, 만약 그 값이 n이 나누어 떨어지는 경우메만 남겨두고, 그 배열의 길이 값을 구해준다. <br><br>

## ✔️ What I learned: <br> 
- js에서도 제곤근 연산자는 '**'이다. <br>
- js에서 제곱근 값 구하는 법<br>
1. Math.sqrt()<br>
2. ** 연산자 <br>
- js의 inInteger함수!!! Numebr 라이브러리에 존재하는함수임<br>
- 만약 n의 값들 1부터 n까지 순서대로 배열에 넣어 배열을 만들어 특정한 값을 남기고 싶으면, Array(n).fill(1).map((v,idx)=>v+idx)로 나타낼 수 있다. 그리고 남길 부분은 filter 함수로 남겨준다. <br><br>
