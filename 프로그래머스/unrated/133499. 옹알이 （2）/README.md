# [unrated] 옹알이 (2) - 133499 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/133499) 

### 성능 요약

메모리: 10.3 MB, 시간: 0.05 ms

### 구분

코딩테스트 연습 > 연습문제

### 채점결과

Empty

### 문제 설명

<p>머쓱이는 태어난 지 11개월 된 조카를 돌보고 있습니다. 조카는 아직 "aya", "ye", "woo", "ma" 네 가지 발음과 네 가지 발음을 조합해서 만들 수 있는 발음밖에 하지 못하고 연속해서 같은 발음을 하는 것을 어려워합니다. 문자열 배열 <code>babbling</code>이 매개변수로 주어질 때, 머쓱이의 조카가 발음할 수 있는 단어의 개수를 return하도록 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>babbling</code>의 길이 ≤ 100</li>
<li>1 ≤ <code>babbling[i]</code>의 길이 ≤ 30</li>
<li>문자열은 알파벳 소문자로만 이루어져 있습니다.</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>babbling</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>["aya", "yee", "u", "maa"]</td>
<td>1</td>
</tr>
<tr>
<td>["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]</td>
<td>2</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>["aya", "yee", "u", "maa"]에서 발음할 수 있는 것은 "aya"뿐입니다. 따라서 1을 return합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>["ayaye", "uuuma", "yeye", "yemawoo", "ayaayaa"]에서 발음할 수 있는 것은 "aya" + "ye" = "ayaye", "ye" + "ma" + "woo" = "yemawoo"로 2개입니다. "yeye"는 같은 발음이 연속되므로 발음할 수 없습니다. 따라서 2를 return합니다.</li>
</ul>

<hr>

<h5>유의사항</h5>

<ul>
<li>네 가지를 붙여 만들 수 있는 발음 이외에는 어떤 발음도 할 수 없는 것으로 규정합니다. 예를 들어 "woowo"는 "woo"는 발음할 수 있지만 "wo"를 발음할 수 없기 때문에 할 수 없는 발음입니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges  <br><br>

<hr>

## ❤️ 문제핵심: <br>
-> 4개의 문자열이 같은 문자열이 중복되지 않게끔 그것들로만 이루어져있는지 검사하는 것이 중요할 것이다. 또한, 예외가 많을 수 있기 때문에, 예외처리하는 게 중요할 것이다. <br><br>

## 😀 나의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/5d3d3b25-5f5f-416f-b785-eef321a3627a) <br>
-> for문으로 babbling의 요소들에 하나씩 접근해주었다. 그 안이 관건이다. 같은 문자가 2번 반복되는 경우에는 count하지 않으므로 건너띄게 하였다. 그런데, 여기서 2번 말고 3,4번 반복되는 경우에는 어떻게 처리해야할 지 그런 경우가 있을 수도 있는 것이기 때문에!!! 어쨌튼 그리고, 4개의 문자열을 다시 반복문으로 하나씩 접근하면서, 존재하면 공백 ' ' 으로 replace해주었다. ' '으로 해준 이유는 'yayae'이런 예외를 처리해주기 위해서이다. 그리고 마지막에 공백을 모두 ''으로 바꿔주었고, 그럼에도 길이가 0인 경우에는 모든 조건을 만족시키므로 answer값을 1증가시켜주었고, 마지막에 answer값을 최종적으로 return 해주었다. <br><br>

## ⭕ 다른 사람의 풀이: <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/4faecb1f-6c87-421d-9d05-67803ec385c4) <br>
-> 나랑 똑같은 풀이 방법이다! 다만, 중복 처리를 그냥 for문 안에서 위와 같이 처리해줘도 된다는 것. 또한, 공백을 제거하는 것은 strip함수를 이용해서 쓸 수 있다는 것! <br><br>

## ✔️ What I learned: <br> 
- strip()함수: 문자열 내에서, 원하는 문자열 또는 공백을 모두 제거하는 함수이다. <br>
![image](https://github.com/An-jisu/Algorithm/assets/70849122/dcad6e4b-ec9a-440a-93b2-4bc2fd8b2e7e) <br>
-> 위와 같이 사용해주면 되고, lstrip, rstrip도 있다. 
