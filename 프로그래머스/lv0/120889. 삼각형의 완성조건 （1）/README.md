# [level 0] 삼각형의 완성조건 (1) - 120889 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120889?language=javascript) 

### 성능 요약

메모리: 33.4 MB, 시간: 0.04 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

Empty

### 문제 설명

<p>선분 세 개로 삼각형을 만들기 위해서는 다음과 같은 조건을 만족해야 합니다.</p>

<ul>
<li>가장 긴 변의 길이는 다른 두 변의 길이의 합보다 작아야 합니다.</li>
</ul>

<p>삼각형의 세 변의 길이가 담긴 배열 <code>sides</code>이 매개변수로 주어집니다. 세 변으로 삼각형을 만들 수 있다면 1, 만들 수 없다면 2를 return하도록 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li><code>sides</code>의 원소는 자연수입니다.</li>
<li><code>sides</code>의 길이는 3입니다.</li>
<li>1 ≤ <code>sides</code>의 원소 ≤ 1,000</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>sides</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>[1, 2, 3]</td>
<td>2</td>
</tr>
<tr>
<td>[3, 6, 2]</td>
<td>2</td>
</tr>
<tr>
<td>[199, 72, 222]</td>
<td>1</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>가장 큰 변인 3이 나머지 두 변의 합 3과 같으므로 삼각형을 완성할 수 없습니다. 따라서 2를 return합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>가장 큰 변인 6이 나머지 두 변의 합 5보다 크므로 삼각형을 완성할 수 없습니다. 따라서 2를 return합니다.</li>
</ul>

<p>입출력 예 #3</p>

<ul>
<li>가장 큰 변인 222가 나머지 두 변의 합 271보다 작으므로 삼각형을 완성할 수 있습니다. 따라서 1을 return합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges <br><br>

<hr>

## 🎁 나의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/16ba3a7e-9f05-42bc-867e-5b37ce7dcc9f) <br>
-> reduce함수를 통해배열의 모든 요소들을 더하고, 가장 큰 값을빼면 나머지 2변의 길이의 합이 나온다. 그 값이가장 긴 벼의 길이보다 크면 삼각형이 완성된다. 여기서는 삼항연산자로 그 조건을 처리하였다. spread operator의 사용을 잘 익히자!! <br><br>

## ⭕ 다른 사람의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/65f3584f-86c5-4282-aa4e-eea8a80bdf53) <br>
-> 여기서는 변 길이의 크기 비교를 배열을 오름차순으로 정렬 후, 인덱스로 접근하여 처리하였다. 여기서 배열의 요소를 개별 인수로 변환하기 위해 전개 연산자가 사용되었다. 전개연산자를 사용하지 않으면, sides를 단일 인수로 처리하여 원하는 결괏값을 얻을 수 없다. <br><br>

## ✔️ What I learned: <br> 
-> js에서 가장 긴, 짧은 변의 길이를 구해야하는 문제에서는 배열의 요소들을 sort해서 풀 수 있다는 것을 기억하자!!! <br>

<spread operator 전개 연산자> <br>

: 배열 또는 객체를 하나하나 넘기는 용도로 사용 <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/e7ea1a7b-629d-4780-9b98-838e33f55d14) <br>
-> 전개 연산자를 사용하지 않으면, array 전체가 들어가 2차원 배열이 되지만, 전개 연산자를 사용하게 되면 array의 내부 요소 하나하나가 삽입된다. <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/f99dcd0d-096b-4943-9f45-938b5413585f) <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/fb5ba8f5-0ca6-4ced-ab4e-c3cba66080f5) <br>
-> 객체에서도 마찬가지이다. 전개연산자를 이용하면 객체에 각각 접근해서 가져올 수 있게 된다. <br>
--> 전개 연산자는 배열이나 객체의 각각 요소에 접근하기 위해 사용된다는 것!!!! 배열의 최댓값이나 최솟값을 구할 때, 배열의 모든 요소들을 전달해야하니까 전개 연산자를 이용해야 한다.<br>
