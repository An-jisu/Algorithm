# [level 0] 한 번만 등장한 문자 - 120896 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120896?language=javascript) 

### 성능 요약

메모리: 33.5 MB, 시간: 0.17 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

Empty

### 문제 설명

<p>문자열 <code>s</code>가 매개변수로 주어집니다. <code>s</code>에서 한 번만 등장하는 문자를 사전 순으로 정렬한 문자열을 return 하도록 solution 함수를 완성해보세요. 한 번만 등장하는 문자가 없을 경우 빈 문자열을 return 합니다.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>0 &lt; <code>s</code>의 길이 &lt; 1,000</li>
<li><code>s</code>는 소문자로만 이루어져 있습니다.</li>
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
<td>"abcabcadc"</td>
<td>"d"</td>
</tr>
<tr>
<td>"abdc"</td>
<td>"abcd"</td>
</tr>
<tr>
<td>"hello"</td>
<td>"eho"</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>"abcabcadc"에서 하나만 등장하는 문자는 "d"입니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>"abdc"에서 모든 문자가 한 번씩 등장하므로 사전 순으로 정렬한 "abcd"를 return 합니다.</li>
</ul>

<p>입출력 예 #3</p>

<ul>
<li>"hello"에서 한 번씩 등장한 문자는 "heo"이고 이를 사전 순으로 정렬한 "eho"를 return 합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges <br><br>

<hr>

## 🎁 나의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/2d65a845-ca13-4369-9814-1e318c3a96be) <br>
-> s를 배열로 변환하고, count가 1인 문자만 filter를 통해 남긴다. 그리고 sort를 통해 정렬 후 join을 통해 문자열로 반환해주었다. 그런데, js에서 count함수가 존재하는 지 아닌지 모르기 때문에, count함수를 따로 만들어줬다. 문자열과 해당 문자를 인수로 전달하여, 그 문자의 갯수를 세서 return해주는 count함수이다. <br><br>

## ⭕ 다른 사람의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/ad73580b-f006-4051-bc3d-f04545247822) <br>
-> <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/45722469-199f-46a8-bd5b-01bac7e1f457) <br>
-> <br><br>

## ✔️ What I learned: <br> 
<sort()> <br>
- 문자 오름차순: <br>
- 정수 오름차순: <br>
