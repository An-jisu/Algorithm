# [level 1] 이상한 문자 만들기 - 12930 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/12930) 

### 성능 요약

메모리: 10.1 MB, 시간: 0.03 ms

### 구분

코딩테스트 연습 > 연습문제

### 채점결과

Empty

### 문제 설명

<p>문자열 s는 한 개 이상의 단어로 구성되어 있습니다. 각 단어는 하나 이상의 공백문자로 구분되어 있습니다. 각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수, solution을 완성하세요.</p>

<h5>제한 사항</h5>

<ul>
<li>문자열 전체의 짝/홀수 인덱스가 아니라, 단어(공백을 기준)별로 짝/홀수 인덱스를 판단해야합니다.</li>
<li>첫 번째 글자는 0번째 인덱스로 보아 짝수번째 알파벳으로 처리해야 합니다.</li>
</ul>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>s</th>
<th>return</th>
</tr>
</thead>
        <tbody><tr>
<td>"try hello world"</td>
<td>"TrY HeLlO WoRlD"</td>
</tr>
</tbody>
      </table>
<h5>입출력 예 설명</h5>

<p>"try hello world"는 세 단어 "try", "hello", "world"로 구성되어 있습니다. 각 단어의 짝수번째 문자를 대문자로, 홀수번째 문자를 소문자로 바꾸면 "TrY", "HeLlO", "WoRlD"입니다. 따라서 "TrY HeLlO WoRlD" 를 리턴합니다.</p>

<h5>문제가 잘 안풀린다면😢</h5>

<p>힌트가 필요한가요? [코딩테스트 연습 힌트 모음집]으로 오세요! → <a href="https://school.programmers.co.kr/learn/courses/14743?itm_content=lesson12930" target="_blank" rel="noopener">클릭</a></p>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges   <br><br>

<hr>

## ❤️ 문제 핵심: <br>
-> 각 단어를 공백을 기준으로 잘라서 생각할 수 있어야하고, 각 단어가 짝수번째 이면 대문자, 홀수이면 소문자로 바꿀 수 있어야함!!! <br><br>

## 😀 나의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/bd07b0eb-2d31-404b-a592-9aa3ecd450a7) <br>
-> 처음에는 홀수일 때, 소문자로 바꿔주는 lower함수를 넣지 않았다. s가 모두 항상 소문자일 것이라고 생각한 것이다. 그러자, 테스트 케이스가 한 개 빼고 모두 오류가 나는 것이다. 제한사항에 있는 내용들을 잘 살펴보자!!! 글자가 모두 소문자라는 조건이 없다!! <br><br>

## ⭕ 다른 사람의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/10f05541-cbec-4db9-8c0a-88d8a75c3b46) <br>
-> map함수를 활용하여, split한 값들에 대해 lamda함수를 실행하는 것이다. 그리고 마지막에 그 값 공백으로 분리하여 다시 join한 것이다. lamda 함수 안에서는, enumerate를 통해, 단어의 요소들을 리스트로 저장하였고, i에 인덱스를 저장하였다. 각 리스트 요소를 소문자, 대문자로 바꿔주고, 마지막에는 다시 join을 통해 문자열로!<br><br>

## ✔️ What I learned: <br>
-> 문제 속에 답이 있다. 문제를 꼼꼼히, 문제의 제한사항을 잘 보자! 또, 열거형은 문자열의 값과 인덱스를 리스트로 나타낸다는 것!! 열거형, lamda함수 쓰는 거 연습하자.<br><br>
