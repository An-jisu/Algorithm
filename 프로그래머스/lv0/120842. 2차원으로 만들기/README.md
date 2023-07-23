# [level 0] 2차원으로 만들기 - 120842 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120842?language=javascript) 

### 성능 요약

메모리: 33.4 MB, 시간: 0.04 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

Empty

### 문제 설명

<p>정수 배열 <code>num_list</code>와 정수&nbsp;<code>n</code>이 매개변수로 주어집니다. <code>num_list</code>를 다음 설명과 같이 2차원 배열로 바꿔 return하도록 solution 함수를 완성해주세요.</p>

<p><code>num_list</code>가 [1, 2, 3, 4, 5, 6, 7, 8] 로 길이가 8이고 <code>n</code>이 2이므로 <code>num_list</code>를 2 * 4 배열로 다음과 같이 변경합니다. 2차원으로 바꿀 때에는 num_list의 원소들을 앞에서부터 n개씩 나눠 2차원 배열로 변경합니다.</p>
<table class="table">
        <thead><tr>
<th>num_list</th>
<th>n</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>[1, 2, 3, 4, 5, 6, 7, 8]</td>
<td>2</td>
<td>[[1, 2], [3, 4], [5, 6], [7, 8]]</td>
</tr>
</tbody>
      </table>
<hr>

<h5>제한사항</h5>

<ul>
<li><code>num_list</code>의 길이는&nbsp;<code>n</code>의 배 수개입니다.</li>
<li>0 ≤ <code>num_list</code>의 길이 ≤ 150</li>
<li>2 ≤ <code>n</code> &lt; <code>num_list</code>의 길이</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>num_list</th>
<th>n</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>[1, 2, 3, 4, 5, 6, 7, 8]</td>
<td>2</td>
<td>[[1, 2], [3, 4], [5, 6], [7, 8]]</td>
</tr>
<tr>
<td>[100, 95, 2, 4, 5, 6, 18, 33, 948]</td>
<td>3</td>
<td>[[100, 95, 2], [4, 5, 6], [18, 33, 948]]</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li><code>num_list</code>가 [1, 2, 3, 4, 5, 6, 7, 8] 로 길이가 8이고 <code>n</code>이 2이므로 2 * 4 배열로 변경한 [[1, 2], [3, 4], [5, 6], [7, 8]] 을 return합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li><code>num_list</code>가 [100, 95, 2, 4, 5, 6, 18, 33, 948] 로 길이가 9이고 <code>n</code>이 3이므로 3 * 3 배열로 변경한 [[100, 95, 2], [4, 5, 6], [18, 33, 948]] 을 return합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges  <br><br>

<hr>

## 🎁 나의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/a386cd90-e74d-430c-bbfe-cce4858e1af2) <br>
-> row의 수 만큼 반복하며 배열을 n의 크기만큼 slice하여 answer 배열에 push해주었다. <br><br>

## ⭕ 다른 사람의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/4dd07808-b31e-4463-8625-e8606d4ead13) <br>
-> splice함수로 n개씩 잘라서 push하였다. splice는 원본 배열을 변경하므로 자른 부분은 사라진다. 따라서 길이가 0이 될 때까지 계속 인덱스는 0부터 시작할 것이다. splice의 반환 형태는 배열이다. <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/ed9dac0e-b47d-4b8f-bec6-d58f4eaae729) <br>
-> 배열을 생성해서, []로 채우고, 그 각각을 splice해서 생긴 값을 넣어주었다. 그 반복을 map함수를 통해 수행하였다. <br><br>

## ✔️ What I learned: <br> 
- slice: 배열의 일부분을 추출하여 새로운 배열을 반환/ 원본 배열 변경x/<br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/16767976-7010-4e35-9fbc-b37b036b17bb) <br>
-> end의 앞부분까지 수행한다. <br>
- splice: 배열에서 요소를 추가, 제거 또는 교체/ 원본 배열이 변경O / 제거된 요소, 새로 삽입된 요소 모두 포함 가능<br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/41a2868b-2599-4d20-8546-143e21da57ba) <br>
-> 시작 인덱스, 제거 갯수<br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/0eba946c-676f-4aca-be4c-2cc51ef56d2a <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/461cc070-0b21-4d7d-baef-4620bf2dfd06)


