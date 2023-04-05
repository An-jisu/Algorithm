# [level 0] 옹알이 (1) - 120956 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120956) 

### 성능 요약

메모리: 10.2 MB, 시간: 0.04 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

<br/>정확성: 100.0<br/>합계: 100.0 / 100.0

### 문제 설명

<p>머쓱이는 태어난 지 6개월 된 조카를 돌보고 있습니다. 조카는 아직 "aya", "ye", "woo", "ma" 네 가지 발음을 최대 한 번씩 사용해 조합한(이어 붙인) 발음밖에 하지 못합니다. 문자열 배열 <code>babbling</code>이 매개변수로 주어질 때, 머쓱이의 조카가 발음할 수 있는 단어의 개수를 return하도록 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>babbling</code>의 길이 ≤ 100</li>
<li>1 ≤ <code>babbling[i]</code>의 길이 ≤ 15</li>
<li><code>babbling</code>의 각 문자열에서 "aya", "ye", "woo", "ma"는 각각 최대 한 번씩만 등장합니다.

<ul>
<li>즉, 각 문자열의 가능한 모든 부분 문자열 중에서 "aya", "ye", "woo", "ma"가 한 번씩만 등장합니다.</li>
</ul></li>
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
<td>["aya", "yee", "u", "maa", "wyeoo"]</td>
<td>1</td>
</tr>
<tr>
<td>["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]</td>
<td>3</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>["aya", "yee", "u", "maa", "wyeoo"]에서 발음할 수 있는 것은 "aya"뿐입니다. 따라서 1을 return합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]에서 발음할 수 있는 것은 "aya" + "ye" = "ayaye", "ye", "ye" + "ma" + "woo" = "yemawoo"로 3개입니다. 따라서 3을 return합니다.</li>
</ul>

<hr>

<h5>유의사항</h5>

<ul>
<li>네 가지를 붙여 만들 수 있는 발음 이외에는 어떤 발음도 할 수 없는 것으로 규정합니다. 예를 들어 "woowo"는 "woo"는 발음할 수 있지만 "wo"를 발음할 수 없기 때문에 할 수 없는 발음입니다.</li>
</ul>

<hr>

<p>※ 공지 - 2022년 10월 27일 문제 지문이 리뉴얼되었습니다. 기존에 제출한 코드가 통과하지 못할 수도 있습니다.</p>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges <br><br>

<hr>

## 👑 나의 풀이: <br>
![image](https://user-images.githubusercontent.com/70849122/229978713-34ea8da6-8005-4086-b9a9-92e196a13032.png) <br>
-> 내 풀이는 중첩 반복문을 활용하여 풀었다. 첫번째 for문은 babbling의 요소들에 접근하기 위한 것이고, 두번째 for문은 각 내가 만들어준 w요소에 접근하기 위한 것이다. 만약, babbling의 요소에 w의 요소가 존재하면 ' '로 대체하도록 하였다. 그리고 마지막에 i가 공백인 경우에는 w에 있는 문자열들로만 만든 문자열이므로 count하게 하여 반환하였다. <br>
-> 처음에는 존재하면 그냥 ''공백이 없는 것으로 대체하게끔 하였다. 그러나, 'wyeoo'와 같은 예외처리에 문제가 생겼다. ye가 존재해서 삭제하면 'woo'만 남는 것이다. 'woo'도 존재하므로 ''로 대체하면, 전체적으로는 ''이 되어, 출력해주는 것이다. 하지만, 순서도 고려해주어야 한다. <br>
![image](https://user-images.githubusercontent.com/70849122/229979228-83c2e84b-4e27-44fc-b2d9-a8e72234768c.png) <br>
-> 따라서, 위와 같이 변경해주었다. ''이 아닌 ' '공백으로 대체해 주었다. 그렇다면 'w oo'가 되어 woo가 처리되지 않을 것이다. 그리고 마지막에 카운트할 때에는, ' '을 다시 ''로 바꿔주어 ''인 경우에 카운트 해주도록 하였다. <br><br>

## ⭕ 다른 사람의 풀이: <br>
![image](https://user-images.githubusercontent.com/70849122/229979858-cbd971dd-d30b-4e34-80e1-e9758ee93a6b.png) <br>
-> 


## ✔ What I learned: <br>
