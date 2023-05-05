# [unrated] 둘만의 암호 - 155652 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/155652) 

### 성능 요약

메모리: 10.3 MB, 시간: 0.03 ms

### 구분

코딩테스트 연습 > 연습문제

### 채점결과

Empty

### 문제 설명

<p>두 문자열 <code>s</code>와 <code>skip</code>, 그리고 자연수 <code>index</code>가 주어질 때, 다음 규칙에 따라 문자열을 만들려 합니다. 암호의 규칙은 다음과 같습니다.</p>

<ul>
<li>문자열 <code>s</code>의 각 알파벳을 <code>index</code>만큼 뒤의 알파벳으로 바꿔줍니다.</li>
<li><code>index</code>만큼의 뒤의 알파벳이 <code>z</code>를 넘어갈 경우 다시 <code>a</code>로 돌아갑니다.</li>
<li><code>skip</code>에 있는 알파벳은 제외하고 건너뜁니다.</li>
</ul>

<p>예를 들어 <code>s</code> = "aukks", <code>skip</code> = "wbqd", <code>index</code> = 5일 때, a에서 5만큼 뒤에 있는 알파벳은 f지만 [b, c, d, e, f]에서 'b'와 'd'는 <code>skip</code>에 포함되므로 세지 않습니다. 따라서 'b', 'd'를 제외하고 'a'에서 5만큼 뒤에 있는 알파벳은 [c, e, f, g, h] 순서에 의해 'h'가 됩니다. 나머지 "ukks" 또한 위 규칙대로 바꾸면 "appy"가 되며 결과는 "happy"가 됩니다.</p>

<p>두 문자열 <code>s</code>와 <code>skip</code>, 그리고 자연수 <code>index</code>가 매개변수로 주어질 때 위 규칙대로 <code>s</code>를 변환한 결과를 return하도록 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>5 ≤ <code>s</code>의 길이 ≤ 50</li>
<li>1 ≤ <code>skip</code>의 길이 ≤ 10</li>
<li><code>s</code>와 <code>skip</code>은 알파벳 소문자로만 이루어져 있습니다.

<ul>
<li><code>skip</code>에 포함되는 알파벳은 <code>s</code>에 포함되지 않습니다.</li>
</ul></li>
<li>1 ≤ <code>index</code> ≤ 20</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>s</th>
<th>skip</th>
<th>index</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>"aukks"</td>
<td>"wbqd"</td>
<td>5</td>
<td>"happy"</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1<br>
본문 내용과 일치합니다.</p>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges <br><br>

<hr>

## 😀 처음풀이: <br>
```
def solution(s, skip, index):
    answer = ''
    for i in s:
        a = []
        count = 0
        #index만큼 반복문 돌면서, i값부터의 값들을 a에 넣기
        for j in range(1,index+1):
            a.append(chr(ord(i)+j))
        #a배열 중 skip에 있는 것과 겹치는 것의 개수 구하기
        for k in a:
            if k in skip:
                count+=1
        #index만큼 이동하고 위의 개수만큼 더 이동
        x = chr(ord(i)+index+count)
        #z넘는 경우에 대한 처리
        if x>'z':
            x = chr(ord(x)-26)
        answer+=x
    return answer
``` 
<br>
-> 문제만 봤을 때는 쉬워보였다. 하지만, 생각보다 skip조건을 지켜주기 위해 코드를 짜주는 게 복잡했다. <br>
-> skip문자열을 고려해주기 위해서, index만큼 돌면서 그 사이의 값들을 배열에 넣었다. 배열 중 skip 있는 것과 겹치는 것의 개수를 세기 위해 for문을 돌렸고 count를 해주었다. index만큼 이동하고, count만큼 추가로 더 이동해주었다. 그리고 z보다 커지는 경우에는 앞으로 되돌아가게 처리를 해주었다. <br>
-> 주어진 테스트케이스는 돌아가는데, 뒤에서는 1문제 빼고는 모두 실패하는 것이다. 예외처리에서 문제가 있었다. 
<br>
1. index에 넣을 때도 z를 넘어갈 수 있는 것을 고려하지 않음<br>
-> 그래도 오류가 나서 다른 사람의 풀이를 참고했다. <br>


## ⭕ 다른 사람의 풀이: <br>
![image](https://user-images.githubusercontent.com/70849122/236422729-53679b1a-f584-4c68-b8ba-1a7daf73173e.png) <br>
-> 여기서는 되돌아가는 것의 의미를 나머지로 생각해서 계산해주었다!! 또 여기서는 skip문자를 제거해주는 식으로 풀이를 했고, 아스키코드를 이용하지 않았다.<br><br>

## ✔️ What I learend: <br>
- 이렇게 뭔가 앞으로 되돌아가는 것, 주어진 문자열이나 리스트에서 인덱스 범위를 넘어갈 때!!! 나머지를 이용해서 처리해보자(문자열이나 리스트의 길이로 나눈 나머지) <br>
![image](https://user-images.githubusercontent.com/70849122/236425995-a2c9db13-4e25-48cc-b143-e4cfd05fff08.png) <br>
-> 그리고 replace함수는 이렇게 반환된 값을 저장해주어야 하므로, 위와 같은 형태로 쓰기!!! alpha.replace 이렇게만 쓰면 안됨.
