# [level 1] 문자열 다루기 기본 - 12918 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/12918) 

### 성능 요약

메모리: 10.3 MB, 시간: 0.01 ms

### 구분

코딩테스트 연습 > 연습문제

### 채점결과

Empty

### 문제 설명

<p>문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수, solution을 완성하세요. 예를 들어 s가 "a234"이면 False를 리턴하고 "1234"라면 True를 리턴하면 됩니다.</p>

<h5>제한 사항</h5>

<ul>
<li><code>s</code>는 길이 1 이상, 길이 8 이하인 문자열입니다.</li>
<li><code>s</code>는 영문 알파벳 대소문자 또는 0부터 9까지 숫자로 이루어져 있습니다.</li>
</ul>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>s</th>
<th>return</th>
</tr>
</thead>
        <tbody><tr>
<td>"a234"</td>
<td>false</td>
</tr>
<tr>
<td>"1234"</td>
<td>true</td>
</tr>
</tbody>
      </table>
<h5>문제가 잘 안풀린다면😢</h5>

<p>힌트가 필요한가요? [코딩테스트 연습 힌트 모음집]으로 오세요! → <a href="https://school.programmers.co.kr/learn/courses/14743?itm_content=lesson12918" target="_blank" rel="noopener">클릭</a></p>

<hr>

<ul>
<li>공지 - 2022년 7월 22일 테스트케이스가 추가되었습니다.</li>
<li>공지 - 2022년 7월 22일 제한 사항이 추가되었습니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges  <br><br>


<hr>

## ⭕ 다른 사람의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/f38a97d0-7750-40b1-9049-685e0caf73a3)<br>
-> 길이가 4또는 6인지를 위와 같이 간단하게 확인할 수도 있다는 것!!<br><br>

## ✔️ What I learned: <br> 
-> 문자열.isdigit(): 문자열이 숫자로만 이루어져 있는지를 확인하는 함수이다!!!!!!!!! 나는 처음에 문자 하나가 digit인지 검사하는 함수라고 생각해서 for문 돌려고 
