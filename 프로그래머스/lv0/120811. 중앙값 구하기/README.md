# [level 0] 중앙값 구하기 - 120811 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120811) 

### 성능 요약

메모리: 10.1 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

<br/>정확성: 100.0<br/>합계: 100.0 / 100.0

### 문제 설명

<p>중앙값은 어떤 주어진 값들을 크기의 순서대로 정렬했을 때 가장 중앙에 위치하는 값을 의미합니다. 예를 들어 1, 2, 7, 10, 11의 중앙값은 7입니다. 정수 배열 <code>array</code>가 매개변수로 주어질 때, 중앙값을 return 하도록 solution 함수를 완성해보세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li><code>array</code>의 길이는 홀수입니다.</li>
<li>0 &lt; <code>array</code>의 길이 &lt; 100</li>
<li>-1,000 &lt; <code>array</code>의 원소 &lt; 1,000</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>array</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>[1, 2, 7, 10, 11]</td>
<td>7</td>
</tr>
<tr>
<td>[9, -1, 0]</td>
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
<li>9, -1, 0을 오름차순 정렬하면 -1, 0, 9이고 가장 중앙에 위치하는 값은 0입니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges

<br>
<hr>

## 🎁 나의 코드와 풀이:
def solution(array):
    array.sort()
    return array[len(array)//2]
-> array를 sort함수를 통해 정렬한 후, 길이값의 중간 인덱스에 해당하는 값을 반환한다.

<br>
## ⭕ 다른 사람들의 풀이:

-> sorted함수와 sort함수의 차이 알기!!

<br>
## 👍 What I learned
1. array.sort(): 배열 자체를 정렬, none값을 리턴! 그 자체로 정렬
2. array2 = sorted(array): 배열을 복사해서 정렬하여 새로운 변수 (새로운 리스트 생성), 정렬해서 리턴시켜줌

    some_list = [5, 7, 2, 3, 1]

    print(sorted(some_list))
    print(some_list.sort())
    >> [1,2,3,5,7]
    >> None
    >> 
