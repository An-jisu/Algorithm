# [level 1] 문자열 내 마음대로 정렬하기 - 12915 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/12915) 

### 성능 요약

메모리: 10.3 MB, 시간: 0.03 ms

### 구분

코딩테스트 연습 > 연습문제

### 채점결과

Empty

### 문제 설명

<p>문자열로 구성된 리스트 strings와, 정수 n이 주어졌을 때, 각 문자열의 인덱스 n번째 글자를 기준으로 오름차순 정렬하려 합니다. 예를 들어 strings가 ["sun", "bed", "car"]이고 n이 1이면 각 단어의 인덱스 1의 문자 "u", "e", "a"로 strings를 정렬합니다.</p>

<h5>제한 조건</h5>

<ul>
<li>strings는 길이 1 이상, 50이하인 배열입니다.</li>
<li>strings의 원소는 소문자 알파벳으로 이루어져 있습니다.</li>
<li>strings의 원소는 길이 1 이상, 100이하인 문자열입니다.</li>
<li>모든 strings의 원소의 길이는 n보다 큽니다.</li>
<li>인덱스 1의 문자가 같은 문자열이 여럿 일 경우, 사전순으로 앞선 문자열이 앞쪽에 위치합니다.</li>
</ul>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>strings</th>
<th>n</th>
<th>return</th>
</tr>
</thead>
        <tbody><tr>
<td>["sun", "bed", "car"]</td>
<td>1</td>
<td>["car", "bed", "sun"]</td>
</tr>
<tr>
<td>["abce", "abcd", "cdx"]</td>
<td>2</td>
<td>["abcd", "abce", "cdx"]</td>
</tr>
</tbody>
      </table>
<h5>입출력 예 설명</h5>

<p><strong>입출력 예 1</strong><br>
"sun", "bed", "car"의 1번째 인덱스 값은 각각 "u", "e", "a" 입니다. 이를 기준으로 strings를 정렬하면 ["car", "bed", "sun"] 입니다.</p>

<p><strong>입출력 예 2</strong><br>
"abce"와 "abcd", "cdx"의 2번째 인덱스 값은 "c", "c", "x"입니다. 따라서 정렬 후에는 "cdx"가 가장 뒤에 위치합니다. "abce"와 "abcd"는 사전순으로 정렬하면 "abcd"가 우선하므로, 답은 ["abcd", "abce", "cdx"] 입니다.</p>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges   <br><br>

<hr>

## ❤️ 문제 핵심: <br>
-> 여기서는, 특정 인덱스를 기준으로 / 그리고 같은 경우 사전순으로 정렬해주는 그 제한 사항을 유심히 살피는 게 중요한 문제다. <br><br>

## 😀 나의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/0c194aad-ca22-487c-960e-b39231b38043) <br>
-> '인덱스 1의 문자가 같은 문자열이 여럿 일 경우, 사전순으로 앞선 문자열이 앞쪽에 위치합니다.'이 조건을 고려하지 않아서, 두 번째 테스트케이스에서 오류가 났다. 따라서 위와 같이 strings자체를 아예 처음부터 사전순으로 정렬 이후 처리를 하게끔 하였다. <br><br>

## ✔️ What I learned: <br>
-> ~ 한 경우 사전 순으로 정렬한다 와 같은 문제에서: 처리 이전에 사전 순 정렬을 먼저 해주자!!!!! <br>
-> 특정 인덱스의 값을 기준으로 정렬할 때, lambda함수를 이용할 수 있다는 것!! <br><br>
