# [unrated] 카드 뭉치 - 159994 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/159994) 

### 성능 요약

메모리: 10.1 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > 연습문제

### 채점결과

Empty

### 문제 설명

<p>코니는 영어 단어가 적힌 카드 뭉치 두 개를 선물로 받았습니다. 코니는 다음과 같은 규칙으로 카드에 적힌 단어들을 사용해 원하는 순서의 단어 배열을 만들 수 있는지 알고 싶습니다.</p>

<ul>
<li>원하는 카드 뭉치에서 카드를 순서대로 한 장씩 사용합니다.</li>
<li>한 번 사용한 카드는 다시 사용할 수 없습니다.</li>
<li>카드를 사용하지 않고 다음 카드로 넘어갈 수 없습니다.</li>
<li>기존에 주어진 카드 뭉치의 단어 순서는 바꿀 수 없습니다.</li>
</ul>

<p>예를 들어 첫 번째 카드 뭉치에 순서대로 ["i", "drink", "water"], 두 번째 카드 뭉치에 순서대로 ["want", "to"]가 적혀있을 때 ["i", "want", "to", "drink", "water"] 순서의 단어 배열을 만들려고 한다면 첫 번째 카드 뭉치에서 "i"를 사용한 후 두 번째 카드 뭉치에서 "want"와 "to"를 사용하고 첫 번째 카드뭉치에 "drink"와 "water"를 차례대로 사용하면 원하는 순서의 단어 배열을 만들 수 있습니다.</p>

<p>문자열로 이루어진 배열 <code>cards1</code>, <code>cards2</code>와 원하는 단어 배열&nbsp;<code>goal</code>이 매개변수로 주어질 때, <code>cards1</code>과 <code>cards2</code>에 적힌 단어들로 <code>goal</code>를 만들 있다면 "Yes"를, 만들 수 없다면 "No"를 return하는 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>cards1</code>의 길이, <code>cards2</code>의 길이 ≤ 10

<ul>
<li>1 ≤ <code>cards1[i]</code>의 길이, <code>cards2[i]</code>의 길이 ≤ 10</li>
<li><code>cards1</code>과 <code>cards2</code>에는 서로 다른 단어만 존재합니다.</li>
</ul></li>
<li>2 ≤ <code>goal</code>의 길이 ≤ <code>cards1</code>의 길이 + <code>cards2</code>의 길이

<ul>
<li>1 ≤ <code>goal[i]</code>의 길이 ≤ 10</li>
<li><code>goal</code>의 원소는 <code>cards1</code>과 <code>cards2</code>의 원소들로만 이루어져 있습니다.</li>
</ul></li>
<li><code>cards1</code>, <code>cards2</code>, <code>goal</code>의 문자열들은 모두 알파벳 소문자로만 이루어져 있습니다.</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>cards1</th>
<th>cards2</th>
<th>goal</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>["i", "drink", "water"]</td>
<td>["want", "to"]</td>
<td>["i", "want", "to", "drink", "water"]</td>
<td>"Yes"</td>
</tr>
<tr>
<td>["i", "water", "drink"]</td>
<td>["want", "to"]</td>
<td>["i", "want", "to", "drink", "water"]</td>
<td>"No"</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<p>본문과 같습니다.</p>

<p>입출력 예 #2</p>

<p><code>cards1</code>에서 "i"를 사용하고 <code>cards2</code>에서 "want"와 "to"를 사용하여 "i want to"까지는 만들 수 있지만 "water"가 "drink"보다 먼저 사용되어야 하기 때문에 해당 문장을 완성시킬 수 없습니다. 따라서 "No"를 반환합니다.</p>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges <br><br>

<hr>

## ❤️ 문제 핵심: <br>
- goal 문자열 완성/ 원하는 카드 뭉치에서 시작/ 0번째 인덱스의 값과만 비교해야함<br>
- cards1과 cards2 중 하나라도 먼저 리스트가 비어진 경우에 대한 처리도 해주어야 함! 값이 비어있는데, 비교하려고하면 오류가 남남<br><br>

## 😀 나의 풀이: <br>
```
def solution(cards1, cards2, goal):
    for i in goal:
        #cards1 리스트를 다 쓴 경우
        if (len(cards1)==0):
            #cards2 리스트에서 계속 비교해주면서, 다르면 return no
            if(i!=cards2[0]):
                return "No"
            else:
                del cards2[0]

        #cards2 리스트를 다 쓴 경우
        elif (len(cards2)==0):
            #cards1 리스트에서 계속 비교해주면서, 다르면 return no
            if(i!=cards1[0]):
                return "No"
            else:
                del cards1[0]

        #아직 둘 다 남아있는 경우 
        else:
            #cards1의 0번째나 cards2의 0번째에 없으면, return "No"/ 
            if (i!=cards1[0]) and (i!=cards2[0]):
                return "No"      
            else:
                #cards1에 있던 경우
                if (i==cards1[0]):
                    del cards1[0]
                #cards2에 있던 경우 
                if (i==cards2[0]):
                    del cards2[0]



    #반복문 끝까지 실행했으면, 모두 성공한 경우- return "Yes"
    return "Yes"
``` <br>
1. 하나의 리스트를 다 쓴 경우를 제외하고, 아직 두 리스트 모두 요소가 남아있는 경우에 대해서 먼저 처리하였다. <br>
- 반복문 돌면서 goal의 요소들에 하나씩 접근한다. 그 값을 cards1[0]와 cards2[0]와 비교한다. 그래서 그 둘 다와 같지 않으면, 카드를 순서대로 접근한다는 중요한 조건을 만족시킬 수 없으므로, 목적을 도달할 수 없어서 return "No"
- 그렇지 않은 경우에는, 둘 중 하나에는 같은 값이 존재하므로 성공이다. 하지만 계속 0번째 인덱스와 비교해주기 위해서는 성공 후, 가장 앞의 요소를 삭제해주어야 한다. 따라서, cards1, cards2 어디서 성공했는지에 따라, 적절한 리스트의 요소를 삭제해준다. 
2. 반복문 끝까지 수행했는데, return "No"가 되지 않았다면, 목표 문자열을 모두 만든 것이므로, return "Yes" 한다. <br>
3. 이제는, 한 뭉치 라도 요소가 다 쓰인 경우에 대한 처리를 한다. cards1인 경우 cards2인 경우 나눠준다. 다 쓴 뭉치를 제외하고, 나머지 뭉치에서 계속해서 넣어주고, 0번째 인덱스와 같지않으면 또, No 반환해준다. <br><br>

## ⭕ 다른 사람의 풀이: <br>
![image](https://user-images.githubusercontent.com/70849122/236111259-bd655ca5-86d9-4e81-9b61-3f7a1f2724ca.png) <br>
-> 이렇게 길게 안쓰고, 아예 그냥 길이와 일치하는지를 한 번에 검사해도 되겠구나!!!!<br><br>

## ✔️ What I learned: <br>
1. 파이썬 리스트 요소 삭제함수
- del: del 리스트명[인덱스]/ 인덱스로 삭제 <br>
- remove: list.remove("요소") / 항목의 값을 삭제 <br>
- pop: 리스트.pop(인덱스) / 특정인덱스의 값 삭제하고 반환 <br>
