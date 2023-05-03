# [unrated] 달리기 경주 - 178871 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/178871#qna) 

### 성능 요약

메모리: 10.3 MB, 시간: 0.01 ms

### 구분

코딩테스트 연습 > 연습문제

### 채점결과

Empty

### 문제 설명

<p>얀에서는 매년 달리기 경주가 열립니다. 해설진들은 선수들이 자기 바로 앞의 선수를 추월할 때 추월한 선수의 이름을 부릅니다. 예를 들어 1등부터 3등까지 "mumu", "soe", "poe" 선수들이 순서대로 달리고 있을 때, 해설진이 "soe"선수를 불렀다면 2등인 "soe" 선수가 1등인 "mumu" 선수를 추월했다는 것입니다. 즉 "soe" 선수가 1등, "mumu" 선수가 2등으로 바뀝니다.</p>

<p>선수들의 이름이 1등부터 현재 등수 순서대로 담긴 문자열 배열 <code>players</code>와 해설진이 부른 이름을 담은 문자열 배열 <code>callings</code>가 매개변수로 주어질 때, 경주가 끝났을 때 선수들의 이름을 1등부터 등수 순서대로 배열에 담아 return 하는 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>5 ≤ <code>players</code>의 길이 ≤ 50,000

<ul>
<li><code>players[i]</code>는 i번째 선수의 이름을 의미합니다.</li>
<li><code>players</code>의 원소들은 알파벳 소문자로만 이루어져 있습니다.</li>
<li><code>players</code>에는 중복된 값이 들어가 있지 않습니다.</li>
<li>3 ≤ <code>players[i]</code>의 길이 ≤ 10</li>
</ul></li>
<li>2 ≤ <code>callings</code>의 길이 ≤ 1,000,000

<ul>
<li><code>callings</code>는 <code>players</code>의 원소들로만 이루어져 있습니다.</li>
<li>경주 진행중 1등인 선수의 이름은 불리지 않습니다.</li>
</ul></li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>players</th>
<th>callings</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>["mumu", "soe", "poe", "kai", "mine"]</td>
<td>["kai", "kai", "mine", "mine"]</td>
<td>["mumu", "kai", "mine", "soe", "poe"]</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<p>4등인 "kai" 선수가 2번 추월하여 2등이 되고 앞서 3등, 2등인 "poe", "soe" 선수는 4등, 3등이 됩니다. 5등인 "mine" 선수가 2번 추월하여 4등, 3등인 "poe", "soe" 선수가 5등, 4등이 되고 경주가 끝납니다. 1등부터 배열에 담으면 ["mumu", "kai", "mine", "soe", "poe"]이 됩니다.</p>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges <br><br>

<hr>

## 😀 처음 풀이: <br>
```
def solution(players, callings):
    #callings의 크기만큼 반복문 돌면서 부른 이름의 인덱스 찾아서 앞의 인덱스의 값과 바꿈
    for i in callings: 
        players[players.index(i)-1], players[players.index(i)] = players[players.index(i)], players[players.index(i)-1]
    
    return players
```
![](https://velog.velcdn.com/images/asj1966/post/5b5714f9-e256-408c-a213-777b7c62b2da/image.png) <br>
-> 결과가 왜 안나와..? 어디가 틀린지 도통 모르겠어서, 블로그에 다른 사람들은 어떻게 풀었는지 검색했다. <br>
->  질문 답변 달리면 이 부분 수정하기!<br><br>

## 😀 그 다음 풀이: <br>
```
def solution(players, callings):
    #callings의 크기만큼 반복문 돌면서 부른 이름의 인덱스 찾아서 앞의 인덱스의 값과 바꿈
    for i in callings: 
        idx = players.index(i)
        players[idx], players[idx-1] = players[idx-1], players[idx]
    
    return players
```
![](https://velog.velcdn.com/images/asj1966/post/188b0a71-b401-49af-acbf-0b5950a83a39/image.png) <br>
-> 시간초과 문제가 뜨는 것이다. <br>
-> .index를 사용해서 시간초과가 뜬 것 같다. <br><br>

## 😀 최종 풀이: <br>
-> 딕셔너리를 사용하면 시간초과 오류가 뜨지 않는다고 한다! <br>
![image](https://user-images.githubusercontent.com/70849122/235825991-c305b748-2c08-4657-85b8-83023b1ae3c2.png) <br>
-> 딕셔너리를 이용하여 {선수: 등수}, {등수: 선수}를 만들어주었다. 그리고, 반복문을 돌면서 {선수:등수}딕셔너리를 이용해서, 각 현재 선수와 그 앞 선수의 등수를 입력받았다. 그리고, {등수: 선수} 딕셔너리를 이용하여, 각 등수의 선수를 교환해주었다. 그 다음, {선수: 등수}를 이용해서 업데이트된 선수의 등수도 변경해주었다. 즉, 선수와 등수가 모두 교환되어 각 디셔너리에 반영된 것이다. 그리고 마지막에는, {등수: 선수}딕셔너리에서 등수는 순서대로 되어 있을 것이므로, 그것의 values값을 list로 출력해주었다. <br><br>

##  ⭕ 다른 사람의 풀이: <br>
![image](https://user-images.githubusercontent.com/70849122/235826474-2e8aa3b7-0407-42d2-b68c-6a95404ff4f6.png) <br>
-> 딕셔너리를 하나 이용해서 풀 수도 있다! 인덱스로 접근하지 않고, 등수를 딕셔너리를 통해서 알아내고, 딕셔너리 값의 등수를 업데이트 시켜! 그리고, 그 값을 players에서 <br><br>

## ✔️ What I learned: <br>
1. 파이썬에서, 특정값의 index 찾기 위해서 <br>
-> players.index("내용") 이렇게 사용!! <br>
2. swap은 temp 이용하거나, 두번째 풀이처럼! 순서대로 대입 <br>
3. 리스트를 수정하는 방식은 오류가 뜰 수 있다는 것!!! 딕셔너리 이용하는 것 연습하자!  <br><br>
