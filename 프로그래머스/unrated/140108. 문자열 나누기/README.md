# [unrated] 문자열 나누기 - 140108 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/140108) 

### 성능 요약

메모리: 10.3 MB, 시간: 2.35 ms

### 구분

코딩테스트 연습 > 연습문제

### 채점결과

Empty

### 문제 설명

<p>문자열 <code>s</code>가 입력되었을 때 다음 규칙을 따라서 이 문자열을 여러 문자열로 분해하려고 합니다.</p>

<ul>
<li>먼저 첫 글자를 읽습니다. 이 글자를 x라고 합시다.</li>
<li>이제 이 문자열을 왼쪽에서 오른쪽으로 읽어나가면서, x와 x가 아닌 다른 글자들이 나온 횟수를 각각 셉니다. 처음으로 두 횟수가 같아지는 순간 멈추고, 지금까지 읽은 문자열을 분리합니다.</li>
<li><code>s</code>에서 분리한 문자열을 빼고 남은 부분에 대해서 이 과정을 반복합니다. 남은 부분이 없다면 종료합니다.</li>
<li>만약 두 횟수가 다른 상태에서 더 이상 읽을 글자가 없다면, 역시 지금까지 읽은 문자열을 분리하고, 종료합니다.</li>
</ul>

<p>문자열 <code>s</code>가 매개변수로 주어질 때, 위 과정과 같이 문자열들로 분해하고, 분해한 문자열의 개수를 return 하는 함수 solution을 완성하세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>s</code>의 길이 ≤ 10,000</li>
<li><code>s</code>는 영어 소문자로만 이루어져 있습니다.</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>s</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>"banana"</td>
<td>3</td>
</tr>
<tr>
<td>"abracadabra"</td>
<td>6</td>
</tr>
<tr>
<td>"aaabbaccccabba"</td>
<td>3</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1<br>
<code>s</code>="banana"인 경우 ba - na - na와 같이 분해됩니다.</p>

<p>입출력 예 #2<br>
<code>s</code>="abracadabra"인 경우 ab - ra - ca - da - br - a와 같이 분해됩니다.</p>

<p>입출력 예 #3<br>
<code>s</code>="aaabbaccccabba"인 경우 aaabbacc - ccab - ba와 같이 분해됩니다.</p>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges <br><br>

<hr>

## ❤️ 문제핵심: <br>
-> 문제를 이해하는데 오래걸린 문제... 가장 첫번째 글자 x를 기준으로, 그 후로 하나씩 접근하면서, 그 수까지 x와 x가 아닌 수가 같아지면분리 그 앞의 것들과 비교하는 것임!!!!<br><br>

## 😀 나의 풀이: <br>
![image](https://user-images.githubusercontent.com/70849122/236742527-d0cc10ed-34f5-4cb4-80cc-f71cd2ebc4ab.png) <br>
-> s의 길이만큼 반복하면서, x정하 (x인수, 아닌 수 같아지면 변수들 초기화)시키는 방법으로 분리를 했다. 마지막꺼는 어차피 분리될 것이므로, 마지막 이전까지만 비교하였다. 그리고 마지막꺼는 몇개가 되었던 분리될 터인데, 그 값은 더해주지 않았으므로 마지막에 +1해서 return 한다. <br><br>

## ⭕ 다른 사람의 풀이: <br>
![image](https://user-images.githubusercontent.com/70849122/236743328-8aeb5dd0-ee01-4b8b-83fe-66c4b7210d9e.png) <br>
-> 여기서는 if문을 처음 넣어주어 마지막에 +1해서 return해줄 필요가 없었다. sav1이 num_x, sav2가 not_num_x를 의미한다. <br><br>
