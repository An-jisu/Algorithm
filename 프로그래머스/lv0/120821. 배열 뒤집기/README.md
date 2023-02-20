# [level 0] 배열 뒤집기 - 120821 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120821) 

### 성능 요약

메모리: 10.2 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

<br/>정확성: 100.0<br/>합계: 100.0 / 100.0

### 문제 설명

<p>정수가 들어 있는 배열 <code>num_list</code>가 매개변수로 주어집니다. <code>num_list</code>의 원소의 순서를 거꾸로 뒤집은 배열을 return하도록 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>num_list</code>의 길이 ≤ 1,000</li>
<li>0 ≤ <code>num_list</code>의 원소 ≤ 1,000</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>num_list</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>[1, 2, 3, 4, 5]</td>
<td>[5, 4, 3, 2, 1]</td>
</tr>
<tr>
<td>[1, 1, 1, 1, 1, 2]</td>
<td>[2, 1, 1, 1, 1, 1]</td>
</tr>
<tr>
<td>[1, 0, 1, 1, 1, 3, 5]</td>
<td>[5, 3, 1, 1, 1, 0, 1]</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li><code>num_list</code>가 [1, 2, 3, 4, 5]이므로 순서를 거꾸로 뒤집은 배열 [5, 4, 3, 2, 1]을 return합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li><code>num_list</code>가 [1, 1, 1, 1, 1, 2]이므로 순서를 거꾸로 뒤집은 배열 [2, 1, 1, 1, 1, 1]을 return합니다.</li>
</ul>

<p>입출력 예 #3</p>

<ul>
<li><code>num_list</code>가 [1, 0, 1, 1, 1, 3, 5]이므로 순서를 거꾸로 뒤집은 배열 [5, 3, 1, 1, 1, 0, 1]을 return합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges <br><br>

<hr>

## 🎁 나의 풀이: <br>
-> 배열을 역순으로 정렬해주는 reversed함수를 사용하였다. <br>
-> 처음에 num_list.reverse() 함수는 제대로 작동하지 않았지만, list(reverse(num_list))는 잘 작동하였다. 그 차이는 아래 정리해보겠다. <br><br>

## ⭕ 다른 사람의 풀이: <br>
![](https://velog.velcdn.com/images/asj1966/post/7f5ada47-ab9a-4233-88d7-0b2bd1386526/image.png)<br>
-> 나는 배열의 뒤집은 후, 반환하였다면 여기서는 그냥 거꾸로 요소들을 반환하도록 하였다. <br>
```
>> arr = range(10)
>> arr
[0,1,2,3,4,5,6,7,8,9]
>> arr[::2] # 처음부터 끝까지 두 칸 간격으로
[0,2,4,6,8]
>> arr[1::2] # index 1 부터 끝까지 두 칸 간격으로
[1,3,5,7,9]
>> arr[::-1] # 처음부터 끝까지 -1칸 간격으로 ( == 역순으로)
[9,8,7,6,5,4,3,2,1,0]
>> arr[::-2] # 처음부터 끝까지 -2칸 간격으로 ( == 역순, 두 칸 간격으로)
[9,7,5,3,1]
>> arr[3::-1] # index 3 부터 끝까지 -1칸 간격으로 ( == 역순으로)
[3,2,1,0]
>> arr[1:6:2] # index 1 부터 index 6 까지 두 칸 간격으로
[1,3,5]
```
<br>
-> [::] 마지막이 -이면 역순을 의미함!!! 따라서, [::-1]은 역순으로 처음부터 끝까지 출력한다는 의미이다. <br><br>


## ✔ What I learned: <br>
<reverse() 와 reversed()의 차이: <br>
둘은 모두 요소를 뒤집을 때 사용한다. <br>
1. reverse(): 값을 반환하지 않음 (변수에 담기 불가능), 리스트 함수, 원형을 바꿔놓음 <br>
2. reversed(): 값을 반환함, 파이썬 내장함수, 원형을 바꿔놓지 않음 <br>
-> 내가 쓴 코드처럼 배열을 뒤집는 동시에 반환하려면, reversed()를 써야 함! <br>
