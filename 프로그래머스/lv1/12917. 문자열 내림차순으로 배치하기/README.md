# [level 1] 문자열 내림차순으로 배치하기 - 12917 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/12917) 

### 성능 요약

메모리: 10.2 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > 연습문제

### 채점결과

Empty

### 문제 설명

<p>문자열 s에 나타나는 문자를 큰것부터 작은 순으로 정렬해 새로운 문자열을 리턴하는 함수, solution을 완성해주세요.<br>
s는 영문 대소문자로만 구성되어 있으며, 대문자는 소문자보다 작은 것으로 간주합니다.</p>

<h5>제한 사항</h5>

<ul>
<li>str은 길이 1 이상인 문자열입니다.</li>
</ul>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>s</th>
<th>return</th>
</tr>
</thead>
        <tbody><tr>
<td>"Zbcdefg"</td>
<td>"gfedcbZ"</td>
</tr>
</tbody>
      </table>

> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges  <br><br>

<hr>

## ❤️ 문제 핵심: <br>
-> sort, sorted함수를 적절히 사용할 줄 알아야한다는 것이 핵심<br><br>

## 😀 나의 풀이: <br>
-> 처음엔 직접 list로 바꾸고, sort해주고 join해주었다. str은 sort, sorted함수 사용이 불가능하다고 하여 <br><br>

## ⭕ 다른 사람의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/d93a9611-5cbe-48d1-b07b-269a2ea7309a) <br>
-> 하지만, sort, sorted하면 문자열을 자동으로 list로 바꿔서 정렬해주고 list를 반환해준다는 것. 하지만 그 후 join을 통해서 다시 문자열로!! <br>

## ✔️ What I learned: <br>
- sort(리스트나 문자열 이름) 이런 형태임!!! <br>
- sorted는 반환을 할 때 써줌!!
